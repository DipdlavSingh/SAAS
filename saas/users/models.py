import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from companies.models import Company


# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    dob = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=16)
    company = models.ForeignKey(Company, related_name="members", 
        on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    