from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField('Title', max_length=50)
    details = models.TextField('What to do')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
