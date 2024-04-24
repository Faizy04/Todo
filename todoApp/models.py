from django.db import models
from django.utils import timezone

class Project(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    
class Todo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='todos')
    description = models.TextField()
    STATUS_CHOICES = [
        ('COMPLETE', 'Complete'),
        ('PENDING', 'Pending'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description