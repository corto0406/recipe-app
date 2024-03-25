from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import RecipesRecipe
from .forms import RecipeForm

class RecipesHomeView(View):
    def get(self, request):
        recipes = RecipesRecipe.objects.all()
        return render(request, 'recipes/recipes_home.html', {'recipes': recipes})

class RecipeDetailsView(View):
    def get(self, request, pk):
        recipe = RecipesRecipe.objects.get(pk=pk)
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
        recipes = RecipesRecipe.objects.all()
        return render(request, 'show_all_recipes.html', {'recipes': recipes})

class SearchResultsView(View):
    def get(self, request):
        query = request.GET.get('query')
        if query:
            search_results = RecipesRecipe.objects.filter(title__icontains=query)
        else:
            search_results = RecipesRecipe.objects.all()
        return render(request, 'search_results.html', {'search_results': search_results})    

    def post(self, request):
        query = request.POST.get('search_criteria')
        if query:
            search_results = RecipesRecipe.objects.filter(title__icontains=query)
        else:
            search_results = RecipesRecipe.objects.all()
        return render(request, 'search_results.html', {'search_results': search_results})

class AboutMeView(TemplateView):
    template_name = 'about_me.html'

class AddRecipeView(CreateView):
    model = RecipesRecipe
    template_name = 'add_recipe.html'
    fields = ['title', 'description', 'cooking_time', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
