from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, reverse

from .models import Comment, CommentZone


@login_required
def create(request, cz_id: int):
    response = {
        'success': False
    }
    if request.method == "POST":
        keys = request.POST.keys()
        if 'replyto' in keys:
            comment_source=get_object_or_404(Comment, pk=request.POST['replyto'])
        else:
            comment_zone=get_object_or_404(CommentZone, pk=cz_id)
        if 'body' in keys:
            comment = Comment(
                author=request.user,
                body = request.POST['body'],
            )
            comment.save()
            if 'replyto' in keys:
                comment_source.replies.add(comment)
            else:
                comment_zone.comments.add(comment)
        else:
            response['message'] = 'No body data.'
    else:
        response['message'] = 'No POST data.'
    return JsonResponse(response)


def get(request, id: int):
    comment = get_object_or_404(Comment, pk=id)
    response = {
        'id': comment.pk,
        'author': comment.author.username,
        'body': comment.body,
        'likes': comment.user_liked.count(),
        'publication_date': comment.publication_date,
        'modification_date': comment.modification_date,
    }
    return JsonResponse(response)


@login_required
def edit(request, id: int):
    comment = get_object_or_404(Comment, pk=id)
    response = {
        'success': False,
    }
    if request.method == 'POST':
        if 'body' in request.POST.keys() and len(request.POST['body']) > 0:
            comment.body = request.POST['body']
            comment.save()
            response['success'] = True
        else:
            response['message'] = 'Empty body.'
    else:
        response['message'] = 'No POST data.'
    return JsonResponse(response)


@login_required
def like(request, id: int):
    comment = get_object_or_404(Comment, pk=id)
    if request.user in comment.user_liked.all():
        comment.user_liked.remove(request.user)
    else:
        comment.user_liked.add(request.user)
    response = {
        'success': True,
        'likes': comment.user_liked.count()
    }
    return JsonResponse(response, safe=True)


@login_required
def delete(request, id: int):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    response = {
        'success': True
    }
    return JsonResponse(response)
