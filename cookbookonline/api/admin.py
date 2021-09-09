from django.contrib import admin
from api.models import Profiles
from api.models import Posts
from api.models import Notifications
from api.models import ReceivedNotifications

# Register your models here.
admin.site.register(Profiles)
admin.site.register(Posts)
admin.site.register(Notifications)
admin.site.register(ReceivedNotifications)
