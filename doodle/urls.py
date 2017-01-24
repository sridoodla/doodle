"""doodle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import ContextTemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ContextTemplateView.as_view(template_name='home/index.html', extra_context={'title': 'Home',
                                                                                           'home': True}), name='home'),
    url(r'^about$', ContextTemplateView.as_view(template_name='home/about.html', extra_context={'title': 'About',
                                                                                                'about': True}), name='about'),
    url(r'^resume$', ContextTemplateView.as_view(template_name='home/resume.html', extra_context={'title': 'Resume',
                                                                                                  'resume': True}), name='resume'),
    url(r'^projects$', ContextTemplateView.as_view(template_name='home/projects.html', extra_context={'title': 'Projects',
                                                                                                      'projects': True}), name='projects'),
    url(r'^contact$', ContextTemplateView.as_view(template_name='home/contact.html', extra_context={'title': 'Contact',
                                                                                                    'contact': True}), name='contact'),
]

urlpatterns += staticfiles_urlpatterns()
