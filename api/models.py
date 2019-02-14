import uuid

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from rest_framework.authtoken.models import Token


class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

class Education(models.Model):
    area = models.CharField(max_length=500, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    degree = models.CharField(max_length=500, blank=True, default='')
    end_date = models.DateField()
    institution = models.CharField(max_length=500, blank=True, default='')
    start_date = models.DateField()
    website = models.URLField(max_length=500, blank=True)
    
class Experience(models.Model):
    company = models.CharField(max_length=500, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    name = models.CharField(max_length=500, blank=True, default='')
    position = models.CharField(max_length=500, blank=True, default='')
    start_date = models.DateField()
    summary = models.TextField()
    website = models.URLField(max_length=500, blank=True)

class Interest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500, blank=True, default='')
    link = models.URLField(max_length=500, blank=True)

class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, blank=True, default='')
    url = models.URLField(max_length=500, blank=True)
    name = models.CharField(max_length=500, blank=True, default='')

class Me(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    github = models.URLField(max_length=500, blank=True)
    headline = models.CharField(max_length=500, blank=True, default='')
    linkedin = models.URLField(max_length=500, blank=True)
    location = models.CharField(max_length=500, blank=True, default='')
    medium = models.URLField(max_length=500, blank=True)
    name = models.CharField(max_length=500, blank=True, default='')
    photo_url = models.URLField(max_length=500, blank=True)
    summary = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=500, blank=True)
    
class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=500, blank=True, default='')
    name = models.CharField(max_length=500, blank=True, default='')
    summary = models.TextField()
    url = models.URLField(max_length=500, blank=True)

class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=500, blank=True, default='')
    image_url = models.URLField(max_length=500, blank=True)
    name = models.CharField(max_length=500, blank=True, default='')
    title = models.CharField(max_length=500, blank=True, default='')
    url = models.URLField(max_length=500, blank=True)

class Skill(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=500, blank=True, default='')
    name = models.CharField(max_length=500, blank=True, default='')

class Social(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    platform = models.CharField(max_length=500, blank=True, default='')
    url = models.URLField(max_length=500, blank=True)
    username = models.CharField(max_length=500, blank=True, default='')