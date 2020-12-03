from django.db import models

# Create your models here.

COMPLETION_STATUS = (
    ('todo', 'To Do'),
    ('in_progress', 'In-progress'),
    ('qa', 'Quality Assesment'),
    ('done', 'Done'),
)

PRIORITIES = (
    ('low', 'Low'),
    ('med', 'Medium'),
    ('high', 'High'),
)

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    assignee = models.CharField(max_length=100)
    status = models.CharField(
        choices=COMPLETION_STATUS, default=COMPLETION_STATUS[0][0], max_length=32)
    priority = models.CharField(
        choices=PRIORITIES, default=PRIORITIES[0][0], max_length=32)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)