from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user=models.CharField(max_length=20, unique=True)
    profilepic=models.ImageField(upload_to='profilepic', blank=True)
    text = models.TextField()
    address=models.CharField(max_length=100)
    company=models.CharField(max_length=100, blank=True)

    UTitle = models.TextField(blank=True)
    University = models.TextField(blank=True)

    HTitle = models.TextField(blank=True)
    Highschool = models.TextField(blank=True)

    STitle = models.TextField(blank=True)
    School = models.TextField(blank=True)

    skill1=models.CharField(max_length=100)
    skill2=models.CharField(max_length=100)
    skill3=models.CharField(max_length=100)
    skill4=models.CharField(max_length=100)
    skill5=models.CharField(max_length=100)
    skill6=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("portfolioapp:homeview")

    def __str__(self):
        return self.user


class AboutMe(models.Model):
    user=models.ForeignKey('Profile',on_delete=models.CASCADE)
    text= models.TextField()

    def get_absolute_url(self):
        return reverse("portfolioapp:aboutme")
