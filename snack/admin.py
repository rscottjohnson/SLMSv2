from django.contrib import admin
from .models import Count, Food

# Register your models here.

@admin.register(Count)
class CountAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'author', 'food', 'quantity', 'publish', 'status')
  list_filter = ('status', 'created', 'publish', 'author')
  search_fields = ('title', 'author', 'food')
  prepopulated_fields = {'slug': ('title',)}
  raw_id_fields = ('author',)
  date_hierarchy = 'publish'
  ordering = ('status', 'publish')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
  list_display = ('description', 'category', 'inventory', 'created')
  list_filter = ('description', 'category', 'created')
  search_fields = ('description',)
  date_hierarchy = 'created'
  ordering = ('description', 'created')


