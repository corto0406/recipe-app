from django.test import TestCase
from .models import RecipesRecipe

class RecipeModelTest(TestCase):
    def setUp(self):
        RecipesRecipe.objects.create(title='Test Recipe', description='This is a test recipe', cooking_time=30)

    def test_recipe_title(self):
        recipe = RecipesRecipe.objects.get(id=1)
        self.assertEqual(recipe.title, 'Test Recipe')

    def test_recipe_description(self):
        recipe = RecipesRecipe.objects.get(id=1)
        self.assertEqual(recipe.description, 'This is a test recipe')

    def test_recipe_cooking_time(self):
        recipe = RecipesRecipe.objects.get(id=1)
        self.assertEqual(recipe.cooking_time, 30)
