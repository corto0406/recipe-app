# recipes/views.py

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Recipe

class RecipesHomeView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, 'recipes/recipes_home.html', {'recipes': recipes})

class RecipeDetailsView(View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        return render(request, 'recipes/recipe_details.html', {'recipe': recipe})
