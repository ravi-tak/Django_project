from django.db import models
# for date setting
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    des = models.TextField()
    content = models.TextField()
    date_blog = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag = models.CharField(max_length=100,db_index=True,default='any_name')
    blog = models.ManyToManyField(Blog, related_name='tags')

    def __str__(self):
        return self.tag