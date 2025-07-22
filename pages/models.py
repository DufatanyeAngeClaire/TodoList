from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = [('pending','pending'),
              ('complete','complete'),]
    status = models.CharField(max_length=10, choices=status, default='pending')
    date = models.DateTimeField()

    def __str__(self):
        return self.title  + '' +  self.status

