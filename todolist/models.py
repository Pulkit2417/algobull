from django.core.exceptions import ValidationError
from django.db import models


class ToDoItem(models.Model):
    STATUS = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='OPEN')

    def __str__(self):
        return self.title

    def clean(self):
        today = date.today()

        # Check if the due date is before today's date
        if self.due_date and self.due_date < today:
            raise ValidationError("Due date cannot be before today's date.")

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
