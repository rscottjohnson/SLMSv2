from django import forms
from django.forms import widgets
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.utils import timezone
from .models import Selection

class SelectionCreateForm(forms.ModelForm):
  class Meta:
    model = Selection
    fields = ('lunch_type', 'parent_attendance', 'content')
