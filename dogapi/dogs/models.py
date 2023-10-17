from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


    
class Breed(models.Model):
    DOG_SIZES = [
        ("T", "Tiny"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]


    name = models.CharField(max_length=30, null=True)
#    size = models.CharField(max_length=1, choices=DOG_SIZES, null=True)
#    breed = models.ForeignKey(Breed, related_name='DogBreed')
    friendliness = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], null=True)
    trainability = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], null=True)
    sheddingamount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], null=True)
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], null=True)
    def __str__(self):
        return str(self.id)+ " : " + str(self.name)

class Dog(models.Model):
    name = models.CharField(max_length=30, null=True)
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], null=True)
    breed = models.ForeignKey(Breed, null=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=8, null=True)
    color = models.CharField(max_length=8, null=True)
    favoritefood = models.CharField(max_length=30, null=True)
    favoritetoy = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return str(self.id)+ " : " + str(self.name)