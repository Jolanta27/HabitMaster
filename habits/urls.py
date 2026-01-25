from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('habits/<int:pk>/', views.habit_detail, name='habit_detail'),
    path('progress/', views.habit_progress, name='habit_progress'),
    path('category/<int:pk>/', views.category_habits, name='category_habits'),
]