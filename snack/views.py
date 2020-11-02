from django.shortcuts import render, get_object_or_404
from .models import Count

# Create your views here.

def count_list(request):
  counts = Count.published.all()
  return render(request, 'snack/count/list.html', {'counts': counts})

def count_detail(request, year, month, day, count):
  count = get_object_or_404(Count, slug=count, status='published', publish__year=year, publish__month=month, publish__day=day)
  return render(request, 'snack/count/detail.html', {'count': count})
