from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileModel(models.Model):  
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    CHARACTERFIELD = [
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('son', 'Son'),
    ]
    
    email_token = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    is_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    character = models.CharField(max_length=100, choices=CHARACTERFIELD)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class IssueModel(models.Model):
        CHARACTERFIELD = [
                ('father', 'Father'),
                ('mother', 'Mother'),
                ('son', 'Son'),
            ]   
        issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
        
        title = models.CharField(max_length=100)
        description = models.TextField()
        prefered_char = models.CharField(max_length=100, choices=CHARACTERFIELD)
    
    
        got_relation = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)