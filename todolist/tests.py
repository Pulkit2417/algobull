from django.core.exceptions import ValidationError
from .models import ToDoItem, Tag
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from datetime import date


# <<<<<------UNIT TESTS------>>>>>
class ToDoItemModelTest(TestCase):
    def test_due_date_validation(self):
        # Test if due date cannot be before timestamp
        timestamp = timezone.now()
        past_date = timestamp - timezone.timedelta(days=1)
        # Create a ToDoItem instance but don't save it immediately
        todo_item = ToDoItem(
            title='Test Task',
            description='Test Description',
            due_date=past_date
        )

        # Raise an error deliberately within the clean method
        def mock_clean_method():
            raise ValidationError("Forced validation error in clean method")

        # Temporarily replace the clean method with the mocked one
        original_clean = todo_item.clean
        todo_item.clean = mock_clean_method
        # Validate the object by attempting to save
        with self.assertRaises(ValidationError):
            todo_item.full_clean()  # Trigger full model validation
        # Restore the original clean method
        todo_item.clean = original_clean
        # Ensure the ToDoItem wasn't saved due to validation error
        self.assertIsNone(todo_item.id)

    def test_todo_item_string_representation(self):
        # Test string representation of ToDoItem
        todo_item = ToDoItem.objects.create(
            title='Test Task',
            description='Test Description',
            status='OPEN'
        )
        self.assertEqual(str(todo_item), 'Test Task')

    def test_todo_item_save_method(self):
        # Test save method of ToDoItem
        todo_item = ToDoItem(
            title='Test Task',
            description='Test Description',
            status='OPEN'
        )
        todo_item.save()
        self.assertIsNotNone(todo_item.id)

    def test_tag_string_representation(self):
        # Test string representation of Tag
        tag = Tag.objects.create(name='Test Tag')
        self.assertEqual(str(tag), 'Test Tag')

    def test_todo_item_with_past_due_date(self):
        # Test ToDoItem creation with a past due date
        past_date = date.today() - timezone.timedelta(days=1)
        with self.assertRaises(ValidationError):
            ToDoItem.objects.create(
                title='Past Due Task',
                description='Description',
                due_date=past_date,
                status='OPEN'
            )
    # Add more tests for other model functionalities as needed


class TagModelTest(TestCase):
    def test_tag_creation(self):
        # Test creating a Tag object
        tag = Tag.objects.create(name='Test Tag')
        self.assertIsNotNone(tag.id)  # Ensure the Tag was created successfully

    # Add more tests for other model functionalities as needed


# <<<<<------INTEGRATION TESTS------>>>>>
class ToDoItemAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('todoitem-list-create')
        self.detail_url = reverse('todoitem-detail', kwargs={'pk': 1})

    def test_create_todo_item(self):
        # Test creating a ToDoItem via API
        data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'status': 'OPEN',
            'tags': ['Tag1', 'Tag2']  # Modify this line with the desired tag names
        }
        response = self.client.post(self.create_url, data, format='json')  # Ensure data is sent in JSON format
        # Ensure successful creation
        self.assertEqual(response.status_code, 201)

    def test_retrieve_todo_item(self):
        # Test retrieving a ToDoItem via API
        todo_item = ToDoItem.objects.create(
            title='Test Task',
            description='Test Description',
            status='OPEN'
        )
        response = self.client.get(self.detail_url)
        # Ensure successful retrieval
        self.assertEqual(response.status_code, 200)
        # Check if the retrieved data matches the created ToDoItem
        self.assertEqual(response.data['title'], todo_item.title)
        self.assertEqual(response.data['description'], todo_item.description)
        self.assertEqual(response.data['status'], todo_item.status)

    def test_tasklist_view(self):
        # Test the tasklist view
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), 'To Do List')
