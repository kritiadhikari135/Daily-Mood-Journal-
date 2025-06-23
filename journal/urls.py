from django.urls import path
from . import views

urlpatterns = [
    path('', views.mood_list, name='mood_list'),
    path('add/', views.mood_create, name='mood_create'),
    path('edit/<int:pk>/', views.mood_edit, name='mood_edit'),
    path('delete/<int:pk>/', views.mood_delete, name='mood_delete'),
    path('detail/<int:pk>/', views.mood_detail, name='mood_detail'),
]
