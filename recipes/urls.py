from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include
from .views import (
    RecipesHomeView, RecipeDetailsView, RecipeLoginView,
    ProfileView, CustomLogoutView, LogoutSuccessView,
    ShowAllRecipesView, SearchResultsView
)

app_name = 'recipes'

urlpatterns = [
    path('', RecipesHomeView.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetailsView.as_view(), name='recipe_details'),
    path('login/', RecipeLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Use your custom logout view
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('logout/success/', LogoutSuccessView.as_view(), name='logout_success'),
    path('show-all/', ShowAllRecipesView.as_view(), name='show_all_recipes'),
    path('search/', SearchResultsView.as_view(), name='search_results')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
