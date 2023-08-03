from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from .models import Post
from .forms import EmailPostForm
from mysite.settings import DEFAULT_FROM_EMAIL


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


def post_share(r, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if r.method == "POST":
        form = EmailPostForm(r.POST)
        if form.is_valid():
            cd = form.cleaned_data

            post_url = r.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            msg = f"read post {post.title} at {post_url} \n\n"

            send_mail(subject, msg, DEFAULT_FROM_EMAIL, [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()
    return render(r, "blog/post/share.html", {"post": post, "form": form, "sent": sent})
