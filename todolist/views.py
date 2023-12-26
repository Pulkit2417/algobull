from rest_framework import generics
from .models import ToDoItem, Tag
from .serializers import ToDoItemSerializer, TagSerializer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response


class ToDoItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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
