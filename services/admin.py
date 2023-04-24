from django.contrib import admin
from services.models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','des')

admin.site.register(Service,ServiceAdmin)