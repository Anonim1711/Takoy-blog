from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect('homepage')
            else:
                messages.add_message(request, messages.ERROR, 'User not found.')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})