from django.shortcuts import render
from django.http import HttpResponse
from dogs.models import Dog
from dogs.models import Breed
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import serializers 
from django.core.validators import MinValueValidator, MaxValueValidator

def index(request):
    return HttpResponse("Hello, world testing.")
    
class BreedSerializer(serializers.Serializer):
    DOG_SIZES = [
        ("T", "Tiny"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = serializers.CharField(max_length=30)
    friendliness = serializers.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    trainability = serializers.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    sheddingamount = serializers.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    exerciseneeds = serializers.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])    
    
    def create(self, validated_data):
        return Breed(**validated_data)
        
    def post(self, validated_data):
        return Breed(**validated_data)
    
class DogSerializer(serializers.Serializer):
    name = serializers.CharField(required=False,max_length=30)
    age = serializers.IntegerField(required=False,validators=[MinValueValidator(0),MaxValueValidator(5)])
    breed = serializers.CharField(required=False,max_length=30)
    gender = serializers.CharField(required=False,max_length=8)
    color = serializers.CharField(required=False,max_length=8)
    favoritefood = serializers.CharField(required=False,max_length=30)
    favoritetoy = serializers.CharField(required=False,max_length=30)

   
    def create(self, validated_data):
        return Dog(**validated_data)
    
#    def post(self, dog, validated_data):       
#        dog = Dog(
#            name=validated_data['name'],
#            age=validated_data['age'],
#            gender=validated_data['gender'],
#            color=validated_data['color'],
#            favoritefood=validated_data['favoritefood'],
#            favoritetoy=validated_data['favoritetoy']),
#        dog.save(self)
#        return Dog(**validated_data)
    


    
class DogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    
    def post(self, validated_data):
        return Dog(**validated_data)
    
class BreedViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()