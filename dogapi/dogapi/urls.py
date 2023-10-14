"""
URL configuration for dogapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import  path, include
from django.urls import include, re_path
from dogs import views
from dogapi import controllers
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
from .controllers import DogList, DogDetails, BreedList, BreedDetails



router = routers.SimpleRouter()
router.register(r'dogs', views.DogViewSet)
router.register(r'breed', views.BreedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
#    path('api/dogs/'), DogList.as_view(), name="create"),
    
#    re_path(r'^dogs', csrf_exempt(controllers.DogDetails.as_view())),
#    re_path(r'^dogs/$', DogList.as_view(), name="create"),
#    re_path(r'^dogs/(?P<pk>[0-9]+)/$', DogDetails.as_view(), name="details"),
#    re_path(r'^breeds/$', BreedList.as_view(), name="bcreate"),
#    re_path(r'^breeds/(?P<pk>[0-9]+)/$', BreedDetails.as_view(), name="bdetails"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
