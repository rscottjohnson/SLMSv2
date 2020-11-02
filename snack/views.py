from django.shortcuts import render, get_object_or_404
from .models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# Create your views here.

def count_list(request):
  object_list = Count.published.all()
  # Instantiate a Paginator class with number of objects to display on each page
  paginator = Paginator(object_list, 8)
  page = request.GET.get('page')
  try:
    counts = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page
    counts = paginator.page(1)
  except EmptyPage:
    # If page is out of range, deliver last page
    counts = paginator.page(paginator.num_pages)
  return render(request, 'snack/count/list.html', {'page': page, 'counts': counts})

def count_detail(request, year, month, day, count):
  count = get_object_or_404(Count, slug=count, status='published', publish__year=year, publish__month=month, publish__day=day)
  return render(request, 'snack/count/detail.html', {'count': count})

# Refactor count_list view into the class-based view offered by Django
class CountListView(ListView):
  queryset = Count.published.all()
  context_object_name = 'counts'
  paginate_by = 8
  template_name = 'snack/count/list.html'
