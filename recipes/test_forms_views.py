from django.test import TestCase
from .forms import RecipeForm
from .views import RecipesHomeView
from django.urls import reverse

class RecipeFormTest(TestCase):
    def test_recipe_form_valid(self):
        form_data = {'title': 'Test Recipe', 'description': 'This is a test recipe.'}
        form = RecipeForm(data=form_data)
        is_valid = form.is_valid()
        print(form.errors)
        self.assertTrue(form.is_valid)
    
    def test_recipe_form_invalid(self):
        form_data = {'title': '', 'description': 'This is a test recipe.'}
        form = RecipeForm(data=form_data)
        self.assertFalse(form.is_valid())

class RecipesHomeViewTest(TestCase):
    def test_recipes_home_view(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_home.html')
