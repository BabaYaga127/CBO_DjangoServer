from django.db import models

class Profiles(models.Model):
    ID = models.AutoField(primary_key=True)
    backgroundImg = models.IntegerField()
    avatar = models.IntegerField()
    name = models.CharField(max_length=50)
    gmail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __unicode__(self):
        return self.ID

class Posts(models.Model):
    ID = models.AutoField(primary_key=True)
    ownerId = models.IntegerField()
    status = models.DateField()
    text = models.CharField(max_length=200)
    image = models.IntegerField()
    def __unicode__(self):
        return self.ID

class Notifications(models.Model):
    ID = models.AutoField(primary_key=True)
    postId = models.IntegerField()
    senderId = models.IntegerField()
    type = models.CharField(max_length=1)
    status = models.DateField('%m-%d-%Y')
    comment = models.CharField(max_length=200)
    def __unicode__(self):
        return self.ID

class ReceivedNotifications(models.Model):
    receiverId = models.IntegerField()
    notoficationId = models.IntegerField()
    def __unicode__(self):
        return self.receiverId + ' ' + self.notoficationId
