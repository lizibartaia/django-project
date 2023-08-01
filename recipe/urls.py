from rest_framework import routers
from recipe import views
from django.urls import path,include
from recipe.views import LoginView, LogoutView,RegisterView



router = routers.DefaultRouter()
router.register('recipe',views.RecipeView)
urlpatterns = [
    path('',include(router.urls)),
    path("user/register/", RegisterView.as_view(), name="register"),
    path("user/login/", LoginView.as_view(), name="login"),
    path("user/logout/", LogoutView.as_view(), name="logout"),
]