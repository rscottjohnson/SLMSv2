from snack.views import CountListView
from django.urls import path
from . import views

app_name = 'snack'
urlpatterns = [
  # snack views
  # path('', views.count_list, name='count_list'),
  path('', views.CountListView.as_view(), name='count_list'),
  path('create/', views.count_create, name='count_create'),
  # path('<int:year>/<int:month>/<int:day>/<slug:count>/edit/', views.count_edit, name='count_edit'),
  path('<int:pk>/edit/', views.count_edit, name='count_edit'),
  path('<int:year>/<int:month>/<int:day>/<slug:count>/', views.count_detail, name='count_detail'),
  path('list/', views.food_list, name='food_list'),
  path('list/<int:id>/', views.food_detail, name='food_detail'),
]

# app_name = 'food'
# urlpatterns = [
#   path('', views.food_list, name='food_list'),
# ]