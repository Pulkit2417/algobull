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
        # Check if due_date is before timestamp only if both are not None
        if self.due_date and self.timestamp:
            if self.due_date < self.timestamp.date():
                raise ValidationError("Due Date before Timestamp created")

    def save(self, *args, **kwargs):
        self.full_clean()  # Run full validation before saving
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
