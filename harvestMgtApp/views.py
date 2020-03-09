from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'harvestMgtApp/signup.html', {'form': form})


def home(request):
    return render(request, 'harvestMgtApp/home.html')


def loginuser(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'harvestMgtApp/signup.html', {'form': form})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')