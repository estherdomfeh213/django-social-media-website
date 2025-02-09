from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  id_user = models.IntegerField()
  bio = models.TextField(blank=True)
  profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
  location = models.CharField(max_length=100, blank=True) 
  
  class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  
  def __str__(self):
    return self.user.username