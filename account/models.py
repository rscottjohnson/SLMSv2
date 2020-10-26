from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

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

# Model for user relationships
class Contact(models.Model):
  # user who creates the relationship
  user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
  # user being followed
  user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
  # when the relationship was created
  created = models.DateTimeField(auto_now_add=True, db_index=True)

  class Meta:
    ordering = ('-created',)
  
  def __str__(self):
    return f'{self.user_from} follows {self.user_to}'
  
# Add following field to User dynamically via generic function
user_model = get_user_model()
user_model.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
