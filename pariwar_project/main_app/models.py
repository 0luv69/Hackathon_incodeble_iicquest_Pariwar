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
                   ('daughter', 'Daughter'),
   ('grandfather', 'Grandfather'),
   ('grandmother', 'Grandmother'),
   ('uncle', 'Uncle'),
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
                   ('daughter', 'Daughter'),
   ('grandfather', 'Grandfather'),
   ('grandmother', 'Grandmother'),
   ('uncle', 'Uncle'),

]   
        issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
        
        title = models.CharField(max_length=100)
        description = models.TextField()
        preferred_char = models.CharField(max_length=100, choices=CHARACTERFIELD)
    
    
        got_relation = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)




class ReplyModel(models.Model):
        issued_by = models.ForeignKey(IssueModel, on_delete=models.CASCADE) 
        replied_by = models.ForeignKey(User, on_delete=models.CASCADE)
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        
        
        def _str_(self):
            return self.issued_by.username
        
        
        
class RelationModel(models.Model):
    name = models.CharField(max_length=100)
    issued_by = models.ForeignKey(IssueModel, on_delete=models.CASCADE)
    replied_by = models.ForeignKey(ReplyModel, on_delete=models.CASCADE)
    
    def _str_(self): 
        return self.name 
    
class ChatModel(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(ProfileModel, related_name='reciver', on_delete=models.CASCADE)
    message = models.TextField()
    relation = models.ForeignKey(RelationModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.sender.username