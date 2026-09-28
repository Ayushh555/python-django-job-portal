from django.db import models
from django.contrib.auth.models import User


# 🔹 PROFILE (Role system)
class Profile(models.Model):
    ROLE_CHOICES = (
        ('HR', 'HR'),
        ('JOBSEEKER', 'Job Seeker'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username


# 🔹 COMPANY
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Unknown")   # ✅ added default
    description = models.TextField(default="No description")         # ✅ added default

    def __str__(self):
        return self.name


# 🔹 JOB (MOST IMPORTANT MODEL)
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.IntegerField()
    experience_required = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 🔹 APPLICATION (REPLACES Candidates)
class Application(models.Model):

    STATUS_CHOICES = (
        ('APPLIED', 'Applied'),
        ('SHORTLISTED', 'Shortlisted'),
        ('REJECTED', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    mobile = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"