from django.shortcuts import render
from .models import Project


def homepage(request):
    projects = Project.objects

    return render(request, 'home.html', {'projects': projects.all})
