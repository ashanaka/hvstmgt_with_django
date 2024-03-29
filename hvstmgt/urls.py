"""hvstmgt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from harvestMgtApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('addfarmer/', views.addfarmer, name='addfarmer'),
    path('farmer/addPlants/<str:farmer_id>', views.addFarmerPlants, name='addFarmerPlants'),
    path('farmers/', views.farmers, name='farmers'),
    path('viewPlants/<int:farmer_id>', views.viewPlants, name='viewPlants'),
    path('data/filter', views.filterdata, name='filterdata'),
]
