from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class ContactSubmission(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('feedback', 'Feedback'),
        ('support', 'Technical Support'),
        ('business', 'Business Partnership'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    rating = models.IntegerField()
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.subject} - {self.submitted_at}"