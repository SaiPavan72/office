""" models for project """
from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    """ different roles present in company which developed by super user"""
    role = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.role


class Project(models.Model):
    """ models for project """
    project_name = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.project_name


class Application(models.Model):
    """ models for application where anyone can apply for job"""

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.ForeignKey(Role, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    experiance_in_years = models.IntegerField()
    is_verified = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Employee(models.Model):
    """ models for registering employee who is verified by super user"""
    office = models.OneToOneField(Application, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    image = models.ImageField(upload_to='media/')
    salary = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.office.name


class Team(models.Model):
    """ models for team in company """
    team_name = models.CharField(max_length=100)
    team_lead = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_working = models.ForeignKey(Project, on_delete=models.CASCADE)

    objects = models.Manager()


class Gmail(models.Model):
    """ models for email """
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    reciever = models.ForeignKey(Employee, on_delete=models.CASCADE)

    file = models.FileField(null=True, blank=True)
    body = models.TextField()
    subject = models.CharField(max_length=1000)

    objects = models.Manager()
