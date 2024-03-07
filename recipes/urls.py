from django.urls import path
from .views import RecipesHomeView, RecipeDetailsView

app_name = 'recipes'

urlpatterns = [
    path('', RecipesHomeView.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetailsView.as_view(), name='recipe_details'),
]
