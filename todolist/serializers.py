from rest_framework import serializers, viewsets
from .models import ToDoItem, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ToDoItemSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=50), write_only=True)

    class Meta:
        model = ToDoItem
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])  # Extract tags data

        # Create or retrieve tags based on the input strings
        tags = []
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)

        todo_item = ToDoItem.objects.create(**validated_data)
        todo_item.tags.add(*tags)  # Add tags to the ToDoItem
        return todo_item



class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
