# forms.py
from django import forms
from .models import RecipesRecipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipesRecipe
        fields = ['title', 'description', 'cooking_time']  # Add other fields as needed

# test_forms_views.py
from django.test import TestCase
from .forms import RecipeForm

class RecipeFormTest(TestCase):
    def test_recipe_form_valid(self):
        form_data = {
            'title': 'Test Recipe',
            'description': 'This is a test recipe',
            'cooking_time': 30,
            # Add other required fields here
        }
        form = RecipeForm(data=form_data)
        self.assertTrue(form.is_valid())
