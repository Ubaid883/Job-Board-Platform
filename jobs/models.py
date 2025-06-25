from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Employee Model
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return str(self.user)
    
    
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume/')
    skills = models.TextField()
    
    def __str__(self):
        return str(self.user)
    
# Job Listing Model
class JobListing(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
# Application Model
class JobApplication(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
           ('Applied', 'Applied'),
        ('Reviewed', 'Reviewed'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
        ], default='Applied')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.status