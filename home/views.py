from django.shortcuts import render

from .models import Project


def view_home(request):
    return render(request, 'home/index.html', {'title': 'Home',
                                               'home': True})


def view_about(request):
    return render(request, 'home/about.html', {'title': 'About',
                                               'about': True})


def view_resume(request):
    return render(request, 'home/resume.html', {'title': 'Resume',
                                                'resume': True})


def view_projects(request):
    projects = Project.objects.all()

    return render(request, 'home/projects.html', {'title': 'Projects',
                                                  'projects': projects})


def view_contact(request):
    return render(request, 'home/contact.html', {'title': 'Contact',
                                                 'contact': True})
