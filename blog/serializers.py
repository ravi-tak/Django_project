from rest_framework import serializers
from blog.models import Blog, Tag
from django.contrib.auth.models import User

# create serializers here

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag']

class BlogSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagSerializers(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'des', 'content', 'date_blog', 'author', 'tags']







# for me

# this way also works but author of blog can be accessed by {{author.username}} in template, in above 
# author name is directly accessed

# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']

# class TagSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'

# class BlogSerializers(serializers.ModelSerializer):
#     users = UserSerializers()   // many=True won't be present
#     tags = TagSerializers(many=True, read_only=True)

#     class Meta:
#         model = Blog
#         fields = ['title', 'des', 'content', 'date_blog', 'author', 'tags', 'users']