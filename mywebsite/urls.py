"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from . import views

# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('myresume/', views.my_resume, name='my_resume'),
    path('know_me/', views.know_me, name='know_me'),  # Corrected view function name
    path('knowme/hi/', views.hi, name='hi'),
    path('knowme/myprojects/', views.my_projects, name='my_projects'),
    path('knowme/volunteerwork/', views.volunteer_work, name='volunteer_work'),
    path('knowme/education/', views.education_history, name='education_history'),
]
