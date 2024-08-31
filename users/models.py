from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

class Chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_method = models.TextField()
    photo = models.ImageField(upload_to='dishes/', blank=True, null=True)
    chef = models.ForeignKey(Chef, related_name='dishes', on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.rating} - {self.dish.name}'
    

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f'Recommendation {self.dish.name} for {self.user.username}'


    