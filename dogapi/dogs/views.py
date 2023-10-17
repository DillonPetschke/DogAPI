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
    
class BreedSerializer(serializers.ModelSerializer):
    friendliness = serializers.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    trainability = serializers.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    sheddingamount = serializers.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    exerciseneeds = serializers.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    
    class Meta:
        model = Breed
        fields = '__all__'


#    DOG_SIZES = [
#        ("T", "Tiny"),
#        ("S", "Small"),
#        ("M", "Medium"),
#        ("L", "Large"),
#    
#    name = serializers.CharField(max_length=30)
    
    
#    def create(self, validated_data):
#        return Breed.objects.create(Breed.data)
        
#    def update(self, instance, validated_data):
#        instance.name = validated_data.get('name', instance.name)
#        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
#        instance.trainability = validated_data.get('trainability', instance.trainability)
#        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
#        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
#        return instance
        
#    def post(self, validated_data):
#        return Breed(**validated_data)
    
class DogSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False,max_length=30)
    age = serializers.IntegerField(required=False,validators=[MinValueValidator(0),MaxValueValidator(5)])
#    breed = serializers.CharField(required=False,max_length=8)
    gender = serializers.CharField(required=False)
    color = serializers.CharField(required=False,max_length=8)
    favoritefood = serializers.CharField(required=False,max_length=30)
    favoritetoy = serializers.CharField(required=False,max_length=30)
    
    class Meta:
        model = Dog
        fields = '__all__'

   
#    def create(self, validated_data):
#        return Dog(**validated_data)
    
#    def update(self, instance, validated_data):
#        instance.name = validated_data.get('name', instance.name)
#        instance.age = validated_data.get('age', instance.age)
#        instance.breed = validated_data.get('breed', instance.breed)
#        instance.gender = validated_data.get('gender', instance.gender)
#        instance.color = validated_data.get('color', instance.color)
#        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
#        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
#        return instance
    


    
class DogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
 
#    def update(self, instance ,**validated_data):
#        return Dog.objects.update(**validated_data)

 
#    def update(self, instance, validated_data):
#        instance.name = (validated_data['name'] )
#        instance.save()
#        return instance
    
    
    
#    def create(self, validated_data):
#        return Dog(**validated_data)
    
class BreedViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Breed instances.
    """
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
    
#    def create(self, validated_data):
#        return Breed(**validated_data)
        
#    def list(self, request):
#        pass
        
    
#    def create(self, validated_data):
#        return BreedViewSet.create(**validated_data)