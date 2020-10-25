from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Selection(models.Model):
  # Define variables for choices
  HOT = 'HOT LUNCH'
  COLD = 'COLD LUNCH'
  FIELD_TRIP = 'FIELD TRIP LUNCH'
  LUNCH_TYPES = [
    (HOT, 'Hot Lunch'),
    (COLD, 'Cold Lunch'),
    (FIELD_TRIP, 'Field Trip Lunch'),
  ]
  YES = 'YES'
  NO = 'NO'
  ATTENDANCE_CHOICES = [
    (YES, 'Yes'),
    (NO, 'No'),
  ]
  user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='selections_created', on_delete=models.CASCADE)
  slug = models.SlugField(max_length=200, blank=True)
  lunch_type = models.CharField(
    max_length=20,
    choices=LUNCH_TYPES,
    default=COLD,
  )
  parent_attendance = models.CharField(
    max_length=3,
    choices=ATTENDANCE_CHOICES,
    default=NO,
  )
  content = models.TextField(blank=True)
  created = models.DateField(auto_now_add=True, db_index=True)
  users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='selections_liked', blank=True)
  
  def __str__(self):
    return self.lunch_type

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.lunch_type)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('selections:detail', args=[self.id, self.slug])