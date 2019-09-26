from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView, name='blog'),
    path('<int:pk>/', views.post, name='post_detail'),
]
