from django.contrib import admin
from blog.models import Blog, Tag
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    # Specify the fields to display on the User model admin page
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']


class BlogAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return self.model.all_objects.all()


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(User, CustomUserAdmin)
