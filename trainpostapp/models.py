from django.db import models

# Create your models here.
class ListModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_user = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="")
    good = models.PositiveIntegerField()
    read = models.PositiveIntegerField()
    readuser = models.TextField()    