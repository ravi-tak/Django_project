from blog import views
from django.urls import path
from blog.views import BlogViewSet, TagViewSet, UserViewSet

urlpatterns =[
    path('form/', views.post),
    path('api-user/', UserViewSet),
    path('api-blog/', BlogViewSet),
    path('api-tag/', TagViewSet),
    path('', views.home, name='home'),
]