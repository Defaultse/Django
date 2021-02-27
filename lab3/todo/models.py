from datetime import datetime
from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=255, null=False)
    creation_date = models.DateField(default=datetime.now())
    due_on_date = models.DateField()
    owner = models.CharField(max_length=50, null=False, default="owner")
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{}: {}'.format(self.id, self.task)