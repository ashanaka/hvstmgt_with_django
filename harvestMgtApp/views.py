
from django.contrib.auth import login, authenticate, logout
from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from .forms import SignUpForm, AddFarmerForm, FarmerGrows, MyForm
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
    farmersPlants = FarmerGrows.objects.select_related('plant').values('plant_id').distinct()
    vals = []
    for plantId in farmersPlants:
        vals.append(plantId['plant_id'])

    farmersPlants = Plant.objects.all()

    testObj = FarmerGrows.objects.values('plant').annotate(Sum('amount'))
    return render(request, 'harvestMgtApp/home.html', {'farmersPlants': farmersPlants, 'testObj': testObj, 'vals': vals,})


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
        farmer_id = Farmer.objects.latest('id')
        # print(farmer_id)
        return render(request, 'harvestMgtApp/addFarmerPlants.html', {'farmer_id': farmer_id, 'plants': plants})
    else:
        form = AddFarmerForm()
    return render(request, 'harvestMgtApp/addfarmer.html', {'form': form})


def addFarmerPlants(request, farmer_id):
    plants = Plant.objects.all()
    farmer_id_new = Farmer.objects.get(pk=farmer_id)
    if request.POST:
        if 'submitPlant' in request.POST:
            form2 = FarmerGrows.objects.create(plant=Plant.objects.get(pk=request.POST['plant']), farmer=farmer_id_new, amount=request.POST['amount'])
            form2.save()
            return redirect('home')
        else:
            form2 = FarmerGrows.objects.create(plant=Plant.objects.get(pk=request.POST['plant']), farmer=farmer_id_new, amount=request.POST['amount'])
            form2.save()
            return render(request, 'harvestMgtApp/addFarmerPlants.html', {'form': form2, 'plants': plants, 'farmer_id': farmer_id})
    else:
        form2 = FarmerGrows();
    return render(request, 'harvestMgtApp/addFarmerPlants.html', {'form': form2, 'plants': plants})


# view farmers in a table
def farmers(request):
    farmersList = Farmer.objects.all()
    return render(request, 'harvestMgtApp/farmers.html', {'farmers': farmersList, })


# view the list of plants of a particular farmer
def viewPlants(request, farmer_id):
    plants = FarmerGrows.objects.filter(farmer=farmer_id)
    return render(request, 'harvestMgtApp/viewPlants.html', {'plants': plants, })


# getting filtered data
def filterdata(request):
    farmersPlants = Plant.objects.all()
    districts = Farmer.objects.select_related('district').values('district').distinct()

    if request.POST:
        if request.POST['district'] != '0' and request.POST['plant'] != '0':
            districtLabel = request.POST['district']
            plantLabel = Plant.objects.get(pk=request.POST['plant']).plantName
        else:
            districtLabel = "All"
            plantLabel = "All"
        if request.POST['district'] == '0' and request.POST['plant'] == '0':
            farmers = Farmer.objects.all()
            growingPlants = FarmerGrows.objects.all()
            return render(request, 'harvestMgtApp/filterdata.html', {'farmersPlants': farmersPlants, 'districts': districts, 'farmers': farmers, 'growingPlants': growingPlants, 'districtLabel': districtLabel, 'plantLabel': plantLabel})
        elif request.POST['district'] != '0' and request.POST['plant'] == '0':
            farmers = Farmer.objects.filter(district=request.POST['district'])
            growingPlants = FarmerGrows.objects.all()
            return render(request, 'harvestMgtApp/filterdata.html', {'farmersPlants': farmersPlants, 'districts': districts, 'farmers': farmers, 'growingPlants': growingPlants, 'districtLabel': districtLabel, 'plantLabel': plantLabel})
        elif request.POST['district'] == '0' and request.POST['plant'] != '0':
            farmers = Farmer.objects.all()
            growingPlants = FarmerGrows.objects.filter(plant=request.POST['plant'])
            return render(request, 'harvestMgtApp/filterdata.html', {'farmersPlants': farmersPlants, 'districts': districts, 'farmers': farmers, 'growingPlants': growingPlants, 'districtLabel': districtLabel, 'plantLabel': plantLabel})
        else:
            farmers = Farmer.objects.filter(district=request.POST['district'])
            growingPlants = FarmerGrows.objects.filter(plant=request.POST['plant'])
            return render(request, 'harvestMgtApp/filterdata.html', {'farmersPlants': farmersPlants, 'districts': districts, 'farmers': farmers, 'growingPlants': growingPlants, 'districtLabel': districtLabel, 'plantLabel': plantLabel})
    else:
        districtLabel = "All"
        plantLabel = "All"
        farmers = Farmer.objects.all()
        growingPlants = FarmerGrows.objects.all()
        return render(request, 'harvestMgtApp/filterdata.html', {'farmersPlants': farmersPlants, 'districts': districts, 'farmers': farmers, 'growingPlants': growingPlants, 'districtLabel': districtLabel, 'plantLabel': plantLabel})

