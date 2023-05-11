from django.db import models
from datetime import datetime

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=(
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ))    
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
