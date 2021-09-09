from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Profile
        fileds = ('ID', 'backgroundImg', 'avatar', 'name', 'gmail', 'password')