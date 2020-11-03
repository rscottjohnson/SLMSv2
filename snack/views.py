from django.shortcuts import render, get_object_or_404, redirect
from .models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import CountCreateForm, CountEditForm
from django.contrib import messages
from django.utils.text import slugify
from django.utils import timezone

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

@login_required
def count_create(request):
  if request.method == 'POST':
    # the form is sent
    form = CountCreateForm(data=request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      new_item = form.save(commit=False)
      # assign the user to the item
      # new_item.user=request.user
      new_item.author=request.user
      new_item.slug=slugify(new_item.title)
      new_item.save()
      # create_action(request.user, 'made selection', new_item)
      messages.success(request, 'Selection added successfully')
      # redirect to new created item detail view
      return redirect(new_item.get_absolute_url())
  else:
    # build form with data provided via GET
    form = CountCreateForm(data=request.GET)
  return render(request, 'snack/count/create.html', {'section': 'count', 'form': form})

@login_required
# def count_edit(request, year, month, day, count):
def count_edit(request, pk):
  # count = get_object_or_404(Count, slug=count, status='published', publish__year=year, publish__month=month, publish__day=day)
  count = get_object_or_404(Count, pk=pk)
  if request.method == 'POST':
    form = CountEditForm(request.POST, instance=count)
    # form = CountEditForm(instance=count, data=request.POST)
    # profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save(commit=False)
      count.author=request.user
      count.publish = timezone.now()
      count.save()
      # profile_form.save()
      # Post a message to the user
      messages.success(request, 'Count updated successfully')
      # return redirect('count_detail', pk=count.pk)
      return redirect(count.get_absolute_url())
    else:
      messages.error(request, 'Error updating count')
  else:
    # form = CountEditForm(instance=request.user)
    form = CountEditForm(instance=count)
    # profile_form = ProfileEditForm(instance=request.user.profile)
  return render(request, 'snack/count/edit.html', {'form': form})