from django.urls import path
from . import views
from .views import (
    ToDoItemListCreateAPIView,
    ToDoItemDetailAPIView,
    TagListCreateAPIView,
    TagDetailAPIView,
)


urlpatterns = [
    path('api/todoitems/', ToDoItemListCreateAPIView.as_view(), name='todoitem-list-create'),
    path('api/todoitems/<int:pk>/', ToDoItemDetailAPIView.as_view(), name='todoitem-detail'),

    path('api/tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('api/tags/<int:pk>/', TagDetailAPIView.as_view(), name='tag-detail'),
    path('', views.tasklist, name='tag-detail'),
    
]
