from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipesHomeView.as_view(), name='home'),
]
