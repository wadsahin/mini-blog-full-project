from django.db import models

# Create your models here.
class UserPost(models.Model):
  title = models.CharField(max_length=170)
  desc = models.TextField()