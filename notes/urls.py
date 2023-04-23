from django.urls import path
from notes.views import function_views as views
from notes.views import class_views


urlpatterns = [
    path('', views.about, name='about'),
    path('upload/', views.upload, name='upload'),
    # path('load_data/', views.load_note_data, name='load-data'),
    path('<str:pk>/', views.detail, name='note-detail'),
    path('topic/all/', views.list_all, name='list-all'),
    # path('topic/<str:topic>/', views.topic, name='topic-list'),
    path('topic/<str:topic>/', class_views.TopicListview.as_view(), name='topic-list'),
]
