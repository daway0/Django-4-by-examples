from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post


def post_list(r):
    posts = Post.published.all()
    return render(r, "blog/post/list.html", {"posts": posts})


def post_detail(r, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post Found!")

    return render(r, "blog/post/detail.html", {"post": post})

def post_detail2(r, id):
    try:
        post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    except Post.DoesNotExist:
        raise Http404("No Post Found!")

    return render(r, "blog/post/detail.html", {"post": post})
