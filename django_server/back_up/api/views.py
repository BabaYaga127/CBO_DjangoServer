from django.shortcuts import render
#from rest_framework import viewsets
from .models import Profile
#from serializers import ProfileSerializer

# Create your views here.

#class ProfileViewSet(viewsets.ModelViewSet):
#    queryset = Profile.objects.add()
#    ProfileSerializer

def home(request):
    return render(request, 'index.html')