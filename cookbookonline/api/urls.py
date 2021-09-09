from django.urls import path, include
from rest_framework import routers
from . import views
from .views import ProfilesViewSet
from .views import PostsViewSet
from .views import NotificationsViewSet
from .views import ReceivedNotificationsViewSet

router = routers.DefaultRouter()

router.register('Profiles', ProfilesViewSet)
router.register('Posts', PostsViewSet)
router.register('Notifications', NotificationsViewSet)
router.register('ReceivedNotifications', ReceivedNotificationsViewSet)

urlpatterns = [
    path('show/', views.home),
    path('', include(router.urls)),
]
