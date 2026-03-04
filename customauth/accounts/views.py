from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import User


def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                full_name=form.cleaned_data['full_name'],
                password=form.cleaned_data['password']
            )
            return redirect('login')

    return render(request, 'register.html', {'form': form})


def login_view(request):
    error = None

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid email or password"

    return render(request, 'login.html', {'error': error})


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')