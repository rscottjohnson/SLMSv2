from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.

# Custom manager
class PublishedManager(models.Manager):
  def get_queryset(self):
    return super(PublishedManager, self).get_queryset().filter(status='published')

# Model for Snack Counts
class Count(models.Model):
  STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
  )
  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250, unique_for_date='publish')
  # count creator
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snack_counts')
  # source the food item from the Food model
  food = models.ForeignKey('Food', on_delete=models.CASCADE, related_name='snack_food')
  # number of items (0 to 100) to include as the distributed count
  quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
  # any comments that the author would like to add
  body = models.TextField()
  publish = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

  class Meta:
    ordering = ('-publish',)

  # default representation
  def __str__(self):
    return self.title

  objects = models.Manager() # the default manager
  published = PublishedManager() # custom manager

  def get_absolute_url(self):
    return reverse('snack:count_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

# Model for Snack Foods
class Food(models.Model):
  CATEGORY_CHOICES = (
    ('bars', 'Bars'),
    ('crackers', 'Crackers'),
    ('fruit', 'Fruit'),
    ('granola', 'Granola'),
    ('mix', 'Mix'),
    ('popcorn', 'Popcorn'),
  )
  description = models.CharField(max_length=250)
  category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='bars')
  inventory = models.IntegerField()
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created',)

  # default representation
  def __str__(self):
    return self.description
  
  def get_absolute_url(self):
    return reverse('snack:food_detail', args=[self.pk])

  