import django_filters
from .models import Dish

class DishFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    chef = django_filters.NumberFilter(field_name='chef_id')
    ingredients = django_filters.NumberFilter(field_name='ingredients_id')

    class Meta:
        model = Dish
        fields = ['name', 'chef', 'ingredients']