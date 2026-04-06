from django.db import models

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('ANALYST', 'Analyst'),
        ('VIEWER', 'Viewer'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name