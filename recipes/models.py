from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='recipe_images/') 


    def __str__(self):
        return self.title

