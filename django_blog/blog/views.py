from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        pass
    return render(request, 'blog/profile.html')