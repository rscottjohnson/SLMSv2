from django.urls import path
from . import views

app_name = 'selections'
urlpatterns = [
  path('create/', views.selection_create, name='create'),
  path('detail/<int:id>/<slug:slug>/', views.selection_detail, name='detail'),
  path('like/', views.selection_like, name='like'),
  path('', views.selection_list, name='list'),
]