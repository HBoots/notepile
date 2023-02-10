from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('<str:pk>/', views.detail, name='note-detail'),
    path('topic/all/', views.list_all, name='list-all'),
    path('topic/<str:topic>/', views.topic, name='topic-list'),
]
