from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  # Add this line

def home(request):
    """
    Render the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template for the home page.
    """
    return render(request, 'home.html')

@login_required
def profile(request):
    """
    Render the user's profile page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template for the user's profile page.
    """
    return render(request, 'profile.html')

@login_required
def chocolate_cake(request):
    """
    Render the chocolate cake recipe page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template for the chocolate cake recipe page.
    """
    return render(request, 'chocolate_cake.html')

@login_required
def cakes(request):
    """
    Render the cakes page with a list of available cake recipes.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template for the cakes page.
    """
    return render(request, 'cakes.html')

@login_required
def cheesecake(request):
    """
    Render the cheesecake recipe page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template for the cheesecake recipe page.
    """
    return render(request, 'cheesecake.html')

@login_required
def vanilla_cake(request):
    """
    Render the vanilla cake recipe page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template for the vanilla cake recipe page.
    """
    return render(request, 'vanilla_cake.html')

def register(request):
    """
    Handle user registration and login.

    If the request method is POST, process the registration form and log in the new user.
    If the request method is GET, display the registration form.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template for the registration page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
