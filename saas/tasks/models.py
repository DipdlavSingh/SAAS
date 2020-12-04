import uuid
from django.db import models
from users.models import User
from companies.models import Company


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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    assignee = models.ForeignKey(User, related_name="tasks", blank=True, on_delete=models.CASCADE)
    status = models.CharField(
        choices=COMPLETION_STATUS, default=COMPLETION_STATUS[0][0], max_length=32)
    priority = models.CharField(
        choices=PRIORITIES, default=PRIORITIES[0][0], max_length=32)
    company = models.ForeignKey(Company, related_name="tasks", 
        blank=True, null=True, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)