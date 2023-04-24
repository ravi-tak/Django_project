# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
from services.models import Service

# To render html
def home(request):
    # Object querey to fetch from DB table 
    service_data = Service.objects.all()

    # To pass data dynamiclly
    data = {
        'title': 'Home',
        'body_data': 'Welcome to Home Page once Again',
        'list': ['PHP','Java','Django'],
        'numbers': [10,20,30,40,50],
        'student_details': [
            {'name': 'pradeep','phone': 9216481602},
            {'name': 'pawan','phone': 9478512556},
        ],
        'serviceData': service_data,
    }
    return render(request, 'index.html', data)

def about(request):
    return HttpResponse(
        "<h1>Welcone to About section</h1>"
    )

def course(request):
    return HttpResponse(
        "<h1>Welcome to Course</h1>"
    )
    
def course_details(request, courseId):
    return HttpResponse(courseId)