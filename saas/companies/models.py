import uuid
from django.db import models

# Create your models here.

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    owner = models.OneToOneField('users.User', related_name="owns_company", 
        on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)