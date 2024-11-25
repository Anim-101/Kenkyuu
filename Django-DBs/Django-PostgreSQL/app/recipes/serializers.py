from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError, APIException
from rest_framework import status

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeModel
        fields = ['id', 'title', 'making_time', 'serves', 'ingredients', 'cost', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        recipe = RecipeModel.objects.create(
            title=validated_data['title'],
            making_time=validated_data['making_time'],
            serves=validated_data['serves'],
            ingredients=validated_data['ingredients'],
            cost=validated_data['cost'],
        )
        recipe.save()
        return recipe