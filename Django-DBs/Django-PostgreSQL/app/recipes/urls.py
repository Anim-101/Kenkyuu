from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', RecipeViewSet.as_view(), name='recipe'),
]