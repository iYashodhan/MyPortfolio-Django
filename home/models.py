from django.db import models


class Project(models.Model):

    project_name = models.CharField(max_length=30)
    image = models.ImageField()
    summary = models.CharField(max_length=500)
    github_link = models.CharField(max_length=100)
    time_period = models.CharField(max_length=50)

