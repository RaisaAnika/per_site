from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def my_resume(request):
    return render(request, 'my_resume.html')

def know_me(request):
    return render(request, 'know_me.html')

def hi(request):
    return render(request, 'hi.html')

def my_projects(request):
    return render(request, 'my_projects.html')

def volunteer_work(request):
    return render(request, 'volunteer_work.html')

def education_history(request):
    return render(request, 'education_history.html')
    