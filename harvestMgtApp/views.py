from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, AddFarmerForm, FarmerGrows
from django.contrib.auth.forms import AuthenticationForm
from .models import Plant, Farmer


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
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect('home')
        except AttributeError:
            return render(request, 'harvestMgtApp/login.html', {'error': "Invalid user!", 'form': AuthenticationForm()})
    else:
        form = AuthenticationForm()
    return render(request, 'harvestMgtApp/login.html', {'form': form})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def addfarmer(request):
    plants = Plant.objects.all()
    if request.method == 'POST':
        form = AddFarmerForm(request.POST)
        form.save()
        # form2 = FarmerGrows(request, plant=request.POST['plant'], farmer=request.POST['farmer'].id)
        form2 = FarmerGrows.objects.create(plant=Plant.objects.get(pk=request.POST['plant']), farmer=Farmer.objects.latest('id'))
        form2.save()
        return redirect('home')
    else:
        form = AddFarmerForm()
    return render(request, 'harvestMgtApp/addfarmer.html', {'form': form, 'plants': plants})
