from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post


def post_list(r):
    posts = Post.published.all()
    return render(r, "blog/post/list.html", {"posts": posts})


def post_detail(r, year, month, day, slug):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(r, "blog/post/detail.html", {"post": post})
