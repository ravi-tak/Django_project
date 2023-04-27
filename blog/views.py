from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from blog.models import Blog, Tag
from django.contrib.auth.models import User
from blog.serializers import BlogSerializers, TagSerializers, UserSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from blog.forms import BlogForm

# Create your views here.

# Post API
def post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
        
    return render(request, 'form.html', {'form': form})

# JSON API
@api_view(['GET'])
def BlogViewSet(request):
    if request.method == 'GET':
        queryset = Blog.objects.all()
        serializer = BlogSerializers(queryset, many=True)
        return Response (serializer.data)

@api_view(['GET'])
def TagViewSet(request):
    if request.method == 'GET':
        queryset = Tag.objects.all()
        serializer = TagSerializers(queryset, many=True)
        return Response (serializer.data)
    
@api_view(['GET'])
def UserViewSet(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializers(queryset, many=True)
        return Response (serializer.data)
    
# Displaying data
def home(request):
    res_blog = requests.get('http://127.0.0.1:8000/api-blog/').json()
    data = {
        'title':'home',
        'resBlog':res_blog,
    }
    return render(request, 'home.html', data)

















# for me

# Post API
# def post(request):
#     if request.method=='POST':
#         # title = request.POST.get('title')
#         title = request.POST['title']
#         des = request.POST['des']
#         content = request.POST['content']
#         tag = request.POST['tag']
#         user = request.POST['user']

#         # check existing user
#         author = ''
#         user_data = User.objects.all()
#         for userObject in user_data:
#             if (userObject.username == user):
#                 author = userObject
#         if (author == ''):
#             author = User(username=user) 
#             # save user object first then pass it to blog author
#             author.save()

#         blog_auth = ''
#         blog_data = Blog.objects.all()
#         for blogObject in blog_data:
#             if (blogObject.title == title):
#                 blog_auth = blogObject
#         if (blog_auth == ''):
#             blogs = Blog(title=title, des=des, content=content, author=author)
#             blogs.save()

#         tags = Tag(tag=tag)
#         tags.save()
#         # Direct assignment to the forward side of a many-to-many set is prohibited. Use blog.set() or blog.add() instead
#         tags.blog.add(blogs)
#         return HttpResponseRedirect('/')
        
#     data = {
#         'title': 'form'
#     }
#     return render(request, 'form.html', data)