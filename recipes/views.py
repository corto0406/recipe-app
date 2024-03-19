from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Recipe
from django.contrib.auth.views import LogoutView
import pandas as pd

class RecipesHomeView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, 'recipes/recipes_home.html', {'recipes': recipes})

class RecipeDetailsView(View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        return render(request, 'recipes/recipe_details.html', {'recipe': recipe})

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile.html'

class RecipeLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('recipes:home')

class LogoutSuccessView(TemplateView):
    template_name = 'success.html'

class CustomLogoutView(LogoutView):
    next_page = '/logout/success/'

class ShowAllRecipesView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, 'show_all_recipes.html', {'recipes': recipes})

class SearchResultsView(View):
    def get(self, request):
        query = request.GET.get('query')
        if query:
            search_results = Recipe.objects.filter(title__icontains=query)
        else:
            search_results = Recipe.objects.all()
        return render(request, 'search_results.html', {'search_results': search_results})    

    def post(self, request):
        query = request.POST.get('search_criteria')
        if query:
            search_results = Recipe.objects.filter(title__icontains=query)
        else:
            search_results = Recipe.objects.all()
        return render(request, 'search_results.html', {'search_results': search_results})
