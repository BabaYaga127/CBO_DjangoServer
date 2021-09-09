from django.shortcuts import render
from rest_framework import viewsets
from .models import Profiles
from .models import Posts
from .models import Notifications
from .models import ReceivedNotifications
from .serializers import ProfilesSerializer
from .serializers import PostsSerializer
from .serializers import NotificationsSerializer
from .serializers import ReceivedNotificationsSerializer

# Create your views here.

def home(request):
    return render(request, 'index.html')

class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer

class ReceivedNotificationsViewSet(viewsets.ModelViewSet):
    queryset = ReceivedNotifications.objects.all()
    serializer_class = ReceivedNotificationsSerializer
