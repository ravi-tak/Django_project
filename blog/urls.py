from blog import views
from django.urls import path
from blog.views import ( BlogViewSet,  
                         blog_details,
                         user_blogs, 
                         PostUpdateView,
                         PostDeleteView
)

urlpatterns =[
    path('', views.home, name='home'),
    path('user/<str:username>/', user_blogs, name='user-blogs'),
    path('blog/<int:pk>/', blog_details, name='blog-details'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('post/', views.post, name='post'),
    path('api-blog/', BlogViewSet),
]