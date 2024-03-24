from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include
from .views import (
    RecipesHomeView, RecipeDetailsView, RecipeLoginView,
    ProfileView, CustomLogoutView, LogoutSuccessView,
    ShowAllRecipesView, SearchResultsView, AboutMeView
)
from .views import AddRecipeView

app_name = 'recipes'

urlpatterns = [
    path('', RecipesHomeView.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetailsView.as_view(), name='recipe_details'),
    path('login/', RecipeLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'), 
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('logout/success/', LogoutSuccessView.as_view(), name='logout_success'),
    path('show-all/', ShowAllRecipesView.as_view(), name='show_all_recipes'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('about/', AboutMeView.as_view(), name='about_me'),
    path('add-recipe/', AddRecipeView.as_view(), name='add_recipe'),
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
