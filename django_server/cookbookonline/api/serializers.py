from rest_framework import serializers
from .models import Profiles
from .models import Posts
from .models import Notifications
from .models import ReceivedNotifications

class ProfilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profiles
        fields = ('url', 'ID', 'backgroundImg', 'avatar', 'name', 'gmail', 'password')

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Posts
        fields = ('url', 'ID', 'ownerId', 'status', 'text', 'image')

class NotificationsSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Notifications
        fields = ('url', 'ID', 'postId', 'senderId', 'type', 'status', 'comment')

class ReceivedNotificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReceivedNotifications
        fields = ('url', 'receiverId', 'notificationId')