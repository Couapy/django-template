from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, reverse
from django.views import View

from .models import Comment, CommentZone


@method_decorator(login_required, name='dispatch')
class CommentCreationView(View):
    """Create a comment."""

    def post(self, request, cz_id: int):
        """Create a comment."""
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


@method_decorator(login_required, name='dispatch')
class CommentView(View):
    """Handle a comment."""

    def get(self, request, id):
        """Get comment as JSON."""
        comment = get_object_or_404(Comment, pk=id, author=request.user)
        response = {
            'id': comment.pk,
            'author': comment.author.username,
            'body': comment.body,
            'likes': comment.user_liked.count(),
            'publication_date': comment.publication_date,
            'modification_date': comment.modification_date,
        }
        return JsonResponse(response)

    def post(self, request, id):
        """Like a comment."""
        if 'like' not in request.POST.keys():
            return HttpResponseBadRequest()

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

    def put(self, request, id):
        """Edit a comment."""
        comment = get_object_or_404(Comment, pk=id, author=request.user)
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

    def delete(self, request, id):
        """Delete a comment."""
        comment = get_object_or_404(Comment, pk=id, author=request.user)
        comment.delete()
        response = {
            'success': True
        }
        return JsonResponse(response)
