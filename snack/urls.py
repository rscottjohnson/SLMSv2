from django.urls import path
from . import views

app_name = 'snack'
urlpatterns = [
  # snack views
  path('', views.count_list, name='count_list'),
  path('<int:year>/<int:month>/<int:day>/<slug:count>/', views.count_detail, name='count_detail'),
]