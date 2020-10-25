from django.contrib import admin
from .models import Selection

# Register your models here.

@admin.register(Selection)
class SelectionAdmin(admin.ModelAdmin):
  list_display = ['lunch_type', 'slug', 'parent_attendance', 'created']
  list_filter = ['created']