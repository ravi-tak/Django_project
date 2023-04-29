# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

# To render html
def course(request):
    return HttpResponse(
        "<h1>Welcome to Course</h1>"
    )
    
def course_details(request, courseId):
    return HttpResponse(courseId)