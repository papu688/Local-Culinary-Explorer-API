from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ChefViewSet, IngredientViewSet, DishViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'chefs', ChefViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls))
]