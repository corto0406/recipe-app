# Generated by Django 4.2.10 on 2024-03-06 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images/'),
        ),
    ]
