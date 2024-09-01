from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Chef, Ingredient, Dish, Rating
from .serializers import UserSerializer, ChefSerializer, IngredientSerializer, DishSerializer, RatingSerializer
from .filters import DishFilter
from .permissions import IsAuthenticatedAndReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ChefViewSet(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DishFilter

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedAndReadOnly]




