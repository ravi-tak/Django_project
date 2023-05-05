from django.db import models
from django.db.models.query import QuerySet
# for date setting
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Creating a new model into Blog model with same functionalities as Default User model with modifications
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


# Soft Delete feature
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class Blog(SoftDelete):
    title = models.CharField(max_length=100)
    des = models.TextField()
    content = models.TextField()
    date_blog = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs')
    image = models.ImageField(null=True, blank=True, upload_to='article_pics')

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=100,db_index=True,default='any_name')
    blog = models.ManyToManyField(Blog, related_name='tags')

    def __str__(self):
        return self.tag