from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Selection
from .forms import SelectionCreateForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def selection_create(request):
  if request.method == 'POST':
    # the form is sent
    form = SelectionCreateForm(data=request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      new_item = form.save(commit=False)
      # assign the user to the item
      new_item.user=request.user
      new_item.save()
      messages.success(request, 'Selection added successfully')
      # redirect to new created item detail view
      return redirect(new_item.get_absolute_url())
  else:
    # build form with data provided via GET
    form = SelectionCreateForm(data=request.GET)
  return render(request, 'selections/selection/create.html', {'section': 'selections', 'form': form})

def selection_detail(request, id, slug):
  selection = get_object_or_404(Selection, id=id, slug=slug)
  return render(request, 'selections/selection/detail.html', {'section': 'selections', 'selection': selection})

@ajax_required
@login_required
@require_POST # not allowed (code 405) if request not done via POST
def selection_like(request):
  selection_id = request.POST.get('id')
  action = request.POST.get('action')
  if selection_id and action:
    try:
      selection = Selection.objects.get(id=selection_id)
      if action == 'like':
        selection.users_like.add(request.user)
      else:
        selection.users_like.remove(request.user)
      return JsonResponse({'status':'ok'})
    except:
      pass
  return JsonResponse({'status':'error'})  

@login_required
def selection_list(request):
  selections = Selection.objects.all()
  paginator = Paginator(selections, 15)
  page = request.GET.get('page')
  try:
    selections = paginator.page(page)
  except PageNotAnInteger:
    # if page is not an integer deliver the first page
    selections = paginator.page(1)
  except EmptyPage:
    if request.is_ajax():
      # If the request is AJAX and the page is out of range then return empty page
      return HttpResponse('')
    # If page is out of range deliver last page of results
    selections = paginator.page(paginator.num_pages)
  if request.is_ajax():
    return render(request, 'selections/selection/list_ajax.html', {'section': 'selections', 'selections': selections})
  return render(request, 'selections/selection/list.html', {'section': 'selections', 'selections': selections})
