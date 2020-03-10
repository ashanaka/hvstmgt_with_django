from django.db import models


class Plant(models.Model):
    plantName = models.CharField(max_length=100)

    def __str__(self):
        return self.plantName


class Farmer(models.Model):
    fName = models.CharField(max_length=100)
    nic = models.CharField(max_length=15)
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.fName


class FarmerGrows(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
