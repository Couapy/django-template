from django.shortcuts import render, get_object_or_404

from .models import Post


def list(request):
    posts = Post.objects.filter(available=True).order_by("-publication_date")
    return render(request, 'blog/list.html', context={'posts': posts})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug, available=True)
    return render(request, 'blog/post.html', context={'post': post})
