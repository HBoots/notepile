from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='note-list'),
    path('<str:pk>', views.detail, name='note-detail'),
]
