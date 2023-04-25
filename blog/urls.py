from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('posts/<slug:slug>', views.recipe_detail, name='recipe-detail'),
    path('like/<slug:slug>', views.LikeToggle.as_view(), name='like-recipe'),
    path('favourites/<slug:slug>', views.FavouriteToggle.as_view(), name='favourite-view'),
]