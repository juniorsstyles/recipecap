from django.shortcuts import render, get_object_or_404
from .models import Recipe

def index(request):
    """
    Display the home page with a list of all recipes.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object containing the rendered template.
    """
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def detail(request, recipe_id):
    """
    Display the detail page for a specific recipe.

    Args:
        request (HttpRequest): The request object.
        recipe_id (int): The ID of the recipe.

    Returns:
        HttpResponse: The response object containing the rendered template.
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def add_recipe(request):
    """
    Display the form to add a new recipe and handle the form submission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object containing the rendered template or
        a redirect to the index page upon successful form submission.
    """
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

def edit_recipe(request, recipe_id):
    """
    Display the form to edit an existing recipe and handle the form submission.

    Args:
        request (HttpRequest): The request object.
        recipe_id (int): The ID of the recipe to edit.

    Returns:
        HttpResponse: The response object containing the rendered template or
        a redirect to the detail page upon successful form submission.
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form})

def delete_recipe(request, recipe_id):
    """
    Delete an existing recipe.

    Args:
        request (HttpRequest): The request object.
        recipe_id (int): The ID of the recipe to delete.

    Returns:
        HttpResponse: A redirect to the index page after deletion.
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('index')
