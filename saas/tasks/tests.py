from django.test import TestCase

from .models import Task
from users.models import User


class TaskModelTests(TestCase):

    def test_task_status_invalid(self):
        with self.assertRaises(Exception):
            task = Task(status='random').save()

    def test_task_status_valid(self):
        user = User()
        user.save()
        task = Task(assignee=user,status='todo')
        task.save()
        self.assertIsNotNone(task)
