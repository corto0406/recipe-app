from django.db import models

class RecipesRecipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(max_length=100)

    class Meta:
        managed = True  # Change this from False to True
        db_table = 'recipes_recipe'
