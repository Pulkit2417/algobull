from rest_framework import generics
from .models import ToDoItem, Tag
from .serializers import ToDoItemSerializer, TagSerializer
from django.http import HttpResponse


class ToDoItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


def tasklist(request):
    return HttpResponse("To Do List")