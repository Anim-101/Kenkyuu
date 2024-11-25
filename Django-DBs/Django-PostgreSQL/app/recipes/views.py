from django.shortcuts import render
from .models import *
from .serializers import RecipeSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class RecipeViewSet(APIView):
    permission_classes = (AllowAny,)

    def post(self, requests):
        serializer = RecipeSerializer(data=requests.data)
        try:
            if serializer.is_valid(raise_exception=True):
                recipe = serializer.create(serializer.validated_data)
                data = {
                    "message": "Recipe successfully created!",
                    "recipe": [
                        {
                            "id": recipe.id,
                            "title": recipe.title,
                            "making_time": recipe.making_time,
                            "serves": recipe.serves,
                            "ingredients": recipe.ingredients,
                            "cost": recipe.cost,
                            "created_at": recipe.created_at,
                            "updated_at": recipe.updated_at
                        }
                    ]
                }
                return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            data = {
                "message": "Recipe creation failed!",
                "required": "title, making_time, serves, ingredients, cost",
                }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, requests):
        recipes = RecipeModel.objects.all()
        data = {
            "recipes": [
                {
                    "id": recipe.id,
                    "title": recipe.title,
                    "making_time": recipe.making_time,
                    "serves": recipe.serves,
                    "ingredients": recipe.ingredients,
                    "cost": recipe.cost,
                    "created_at": recipe.created_at,
                    "updated_at": recipe.updated_at
                }
                for recipe in recipes
            ]
        }
        return Response(data, status=status.HTTP_200_OK)
