from django.db import models
from django.conf import settings

# Create your models here.

# Extending the User model with a Profile model
class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  is_staff = models.BooleanField('staff status', default=False)
  guardian_name = models.CharField(max_length=180)
  guardian_email = models.CharField(max_length=254)
  homeroom_teacher = models.CharField(max_length=130)

  
  def __str__(self):
    return f'Profile for user {self.user.username}'
  

