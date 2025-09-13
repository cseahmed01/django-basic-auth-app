# posts/models.py
from django.db import models

class Post(models.Model):
    FILE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    
    title = models.CharField(max_length=200)           # Post title
    short_description = models.TextField()            # Brief description
    file = models.FileField(upload_to='posts/')       # Media file
    file_type = models.CharField(max_length=10, choices=FILE_CHOICES)  # Type of file
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title
