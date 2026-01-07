# djangomyblog\blog\views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blog.utils.markdown import render_markdown
from .forms import CustomUserCreationForm
from blog.models import Post, Comment


def home(request):

    posts = (
        Post.objects
        .filter(status='ON')
        .select_related('user')
        .order_by('-created_at')
    )

    return render(request, "blog/home.html", {"posts": posts})


def about(request):
    return render(request, "blog/about.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status='ON')
    post.content_html = render_markdown(post.content)

    comments = (
        Comment.objects
        .filter(status='ON')
        .filter(post=id)
        .select_related('user')
        .order_by('-created_at')
    )

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments}
    )


@login_required
def new_post(request):

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                user=request.user,
                status='ON'
            )
            return redirect("home")

    return render(request, "blog/new_post.html")


@login_required
def delete_post(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status='ON'
    )

    if post.user != request.user:
        return redirect('home')

    post.status = 'DEL'
    post.save(update_fields=['status'])

    return redirect('home')


@login_required
def edit_post(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status='ON'
    )

    # só o dono pode editar
    if post.user != request.user:
        return redirect('home')

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            post.title = title
            post.content = content
            post.save(update_fields=['title', 'content'])

            return redirect('post_detail', id=post.id)

    return render(request, 'blog/edit_post.html', {
        'post': post
    })


@login_required
def comment_post(request):
    if request.method == "POST":
        postid = request.POST.get("postid")
        comment_text = request.POST.get("comment", "").strip()

        post = get_object_or_404(Post, id=postid, status="ON")

        if comment_text:
            Comment.objects.create(
                comment=comment_text,
                user=request.user,
                post=post,
                status="ON"
            )

        return redirect("post_detail", id=post.id)

    return redirect("home")
