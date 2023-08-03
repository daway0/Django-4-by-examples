from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(r):
    posts = Post.published.all()
    paginator = Paginator(posts, 1)

    page_number = r.GET.get("page", 1)
    try:
        posts_page = paginator.page(page_number)
    except EmptyPage:
        posts_page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts_page = paginator.page(1)
    return render(r, "blog/post/list.html", {"posts_page": posts_page})


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
