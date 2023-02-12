from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('upload/', views.upload, name='upload'),
    # path('load_data/', views.load_note_data, name='load-data'),
    path('<str:pk>/', views.detail, name='note-detail'),
    path('topic/all/', views.list_all, name='list-all'),
    path('topic/<str:topic>/', views.topic, name='topic-list'),
]
