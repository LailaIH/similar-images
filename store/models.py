from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    image = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



