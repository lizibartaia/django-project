from recipe.models import Recipe
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","password"]

class RecipeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "ingredient",
            "time",
            "process",
            "user"
        ]


