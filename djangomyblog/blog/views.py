# djangomyblog\blog\views.py

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from djangomyblog.blog.models import Post

from .forms import CustomUserCreationForm


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

# Só acessa profile() se estiver logado
# Não está logado, vai para '/accounts/login/'


@login_required
def profile(request):
    return render(request, "blog/profile.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
