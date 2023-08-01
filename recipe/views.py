from django.shortcuts import render
from rest_framework import viewsets
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer,UserSerializer
from django.contrib.auth import authenticate,login,logout
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
# Create your views here.

class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RegisterView(generics.GenericAPIView,):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
     

class LoginView(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()

        if user:
            login(request,user)
            return Response(UserSerializer(user).data)
        if user is None:
            raise AuthenticationFailed("user not found")
        if not user.check_password(password):
            raise AuthenticationFailed("incorrect password")
            
        return Response(user,{"error":"wrong credentials"},status=status.HTTP_400_BAD_REQUEST)

  

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        logout(request)
        return Response(status=status.HTTP_200_OK)