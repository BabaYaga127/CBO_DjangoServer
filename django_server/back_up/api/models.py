from django.db import models

# Create your models here.

class Profile(models.Model):
    ID = models.AutoField(primary_key=True)
    backgroundImg = models.IntegerField()
    avatar = models.IntegerField()
    name = models.CharField(max_length=50)
    gmail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __unicode__(self):
        return self.ID
