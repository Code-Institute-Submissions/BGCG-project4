from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('all-recipes/', views.AllRecipes.as_view(), name='all-recipes'),
    path('posts/<slug:slug>', views.recipe_detail, name='recipe-detail'),
    path('like/<slug:slug>', views.LikeToggle.as_view(), name='like-recipe'),
    path('favourite/<slug:slug>', views.FavouriteView.as_view(),
         name='favourite-view'),
    path('favourites/', views.FavouriteView.as_view(), name='favourite-list'),
    path('create-post/', views.create_post, name='create-post'),
    path('your-posts/', views.your_posts_view, name='your-posts-list'),
    path('posts/edit-post/<slug:slug>', views.edit_post, name='edit-post'),
    path('posts/delete-post/<slug:slug>', views.delete_post,
         name='delete-post'),
    path('contact-us/', views.contact_request, name='contact-request'),
]
