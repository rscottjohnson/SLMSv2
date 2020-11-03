from django import forms
from .models import Count, Food

class CountCreateForm(forms.ModelForm):
  class Meta:
    model = Count
    fields = ('title', 'food', 'quantity', 'body', 'status')

class CountEditForm(forms.ModelForm):
  class Meta:
    model = Count
    fields = ('food', 'quantity', 'body', 'status')

class FoodCreateForm(forms.ModelForm):
  class Meta:
    model = Food
    fields = ('description', 'category', 'inventory')

class FoodEditForm(forms.ModelForm):
  class Meta:
    model = Food
    fields = ('description', 'category', 'inventory')