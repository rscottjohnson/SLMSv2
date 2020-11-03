from django import forms
from .models import Count

class CountCreateForm(forms.ModelForm):
  class Meta:
    model = Count
    fields = ('title', 'food', 'quantity', 'body', 'status')

class CountEditForm(forms.ModelForm):
  class Meta:
    model = Count
    fields = ('food', 'quantity', 'body', 'status')