from django.db import models
from django.contrib import auth

from .choices import designation_choices, status_choices, progress_choices
from .imports import ListField

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=False)
    res_address = models.CharField(max_length=200, blank=False)
    personal_contact_no = models.CharField(max_length=10, blank=False)
    emergency_contact_no = models.CharField(max_length=10)
    personal_email = models.EmailField(unique=True, blank=False)
    designation = models.CharField(max_length=100, blank=False, choices=designation_choices, default="Associate")
    salary = models.FloatField(blank=False)
    passport_pic = models.ImageField(upload_to='passport_pic')    # Location where profile_pic is saved
    joining_date = models.DateField(blank=False)
    projects = models.ManyToManyField('Project')


class Project(models.Model):
    assignee = models.ForeignKey(auth.models.User, on_delete=models.DO_NOTHING, related_name="assignee")
    assigned_to = models.ManyToManyField(auth.models.User, through='ProjectMember', related_name='assigned_to')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default='')
    SRS = models.FileField(upload_to='projects/SRS/')
    goals = models.CharField(max_length=255)
    KRA = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=status_choices)
    tasks = models.ManyToManyField('Task', related_name='task')


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="assigned")
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE, related_name="user_project")

    class Meta():
        unique_together = ('project', 'user')

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    progress = models.CharField(max_length=100, choices=progress_choices)

