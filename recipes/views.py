from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  # Add this line

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def chocolate_cake(request):
    return render(request, 'chocolate_cake.html')

@login_required
def cakes(request):
    return render(request, 'cakes.html')

@login_required
def cheesecake(request):
    return render(request, 'cheesecake.html')

@login_required
def vanilla_cake(request):
    return render(request, 'vanilla_cake.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
