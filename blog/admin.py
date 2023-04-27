from django.contrib import admin
from blog.models import Blog, Tag

# Register your models here.
admin.site.register([Blog,Tag])