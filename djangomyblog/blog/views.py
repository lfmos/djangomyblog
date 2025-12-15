# djangomyblog\blog\views.py

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")

# Só acessa profile() se estiver logado
# Não está logado, vai para '/accounts/login/'

@login_required
def profile(request):
    return render(request, "blog/profile.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})