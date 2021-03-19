from django.utils import timezone
from django.db import models


class List(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Todo(models.Model):
    name = models.CharField(max_length=255, null=False)
    creation_date = models.DateField(default=timezone.now)
    due_on_date = models.DateField()
    owner = models.CharField(max_length=50, null=False, default="owner")
    status = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)
