from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Blog
from blog.forms import BlogForm
from blog.serializers import BlogSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic import (UpdateView, DeleteView)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import requests
from django.core.paginator import Paginator, PageNotAnInteger

# Create your views here.

# Post API
@login_required
def post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(request, f'Post Added!')
            return redirect('home')
    else:
        form = BlogForm()
        
    return render(request, 'blog_form.html', {'form': form})


# JSON API
@api_view(['GET'])
def BlogViewSet(request):
    if request.method == 'GET':
        queryset = Blog.objects.all()
        serializer = BlogSerializers(queryset, many=True)
        return Response (serializer.data)
    
    
# Displaying data
def home(request):
    res_blog = requests.get('http://127.0.0.1:8000/api-blog/').json()
    res_blog.reverse()
    # we are creating a Paginator object paginator which will paginate the res_blog queryset in chunks of 5 items per page.
    paginator = Paginator(res_blog, 5)

    # we are getting the current page number from the GET request
    page = request.GET.get('page')
    try:
        # return the requested page object blogs is actually the instance of the Page class returned by the Paginator
        blogs = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.get_page(1)

    data = {
        'title':'home',
        'blogs': blogs
    }
    return render(request, 'home.html', data)


def user_blogs(request, username):
    res_blog = requests.get('http://127.0.0.1:8000/api-blog/').json()
    filtered_blogs = [blog for blog in res_blog if blog['author'].strip().lower() == username.strip().lower()]
    filtered_blogs.reverse()

    paginator = Paginator(filtered_blogs, 5)

    page = request.GET.get('page')
    try:
        blogs = paginator.get_page(page)
    except PageNotAnInteger:
        blogs = paginator.get_page(1)

    data = {
        'title': 'user_blogs',
        'blogs': blogs,
        'username': username
    }
    return render(request, 'user_blogs.html', data)


@api_view(['GET'])
def blog_details(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return render(request, 'blog_details.html')

    serializer = BlogSerializers(blog)
    return render(request, 'blog_details.html', {'data': serializer.data, 'author': blog.author})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'des', 'content', 'image']
    # We need templates folder inside the blog app to work by default
    # <model>_form.html expected while using UpdateView
    template_name = 'blog_form.html'

    # providing author to the form object
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # setting redirect url or we can do in model by get_absolute_url func
    def get_success_url(self):
        messages.success(self.request, f'Post Updated!')
        return reverse_lazy('blog-details', kwargs={'pk': self.object.pk})
    
    # check current user is the post author or not
    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        else:
            return False
        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    # <model>_confirm_form.html expected while using DeleteView
    template_name = 'blog_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, f'Post Deleted!')
        return reverse_lazy('home')
    
    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        else:
            return False
    
    















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