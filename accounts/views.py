from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

def home(request):
    # Handle registration
    if request.method == "POST" and "signup" in request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()

    # Handle login
    if request.method == "POST" and "signin" in request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid username or password"
            return render(request, "accounts/home.html", {"form": form, "error": error})

    return render(request, "accounts/home.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")


def user_logout(request):
    logout(request)
    return redirect('home')
