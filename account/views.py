from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.

# User login view
def user_login(request):
  if request.method == 'POST':
    # Instantiate the form and check if it's valid (user inputs correct, etc.)
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      # Authenticate the user against the database
      user = authenticate(request, 
        username=cd['username'], 
        password=cd['password'])
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponse('Authenticated '\
                              'successfully')
        else:
          return HttpResponse('Disabled account')
      else:
        return HttpResponse('Invalid login')
  else:
    form = LoginForm()
  return render(request, 'account/login.html', {'form': form})

# Check if the user is authenticated
@login_required
# User dashboard view
def dashboard(request):
  return render(request, 'account/dashboard.html', {'section': 'dashboard'})
    