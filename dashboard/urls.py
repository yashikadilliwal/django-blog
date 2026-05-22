from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add_post/', views.add_post, name='add_post'),
    path('categories/', views.categories, name='categories'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:id>/', views.edit_category, name='edit_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('users/', views.users, name='users'),
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    # =======================dashboard crud===========
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    
   ]