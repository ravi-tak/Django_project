from rest_framework import serializers
from blog.models import Blog, Tag
from users.models import Profile

# create serializers here

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag']

class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'image']

class BlogSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagSerializers(many=True, read_only=True)
    date_blog = serializers.DateTimeField(format="%B %d, %Y")
    author_profile = ProfileSerializers(source='author.profile', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'des', 'content', 'date_blog', 'image', 'author', 'tags', 'author_profile']







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