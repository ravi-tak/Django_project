from django import forms
from blog.models import Blog, Tag

class BlogForm(forms.ModelForm):
    tags = forms.CharField(max_length=100)
    
    class Meta:
        model = Blog
        fields = ['title', 'des', 'content', 'tags', 'image']

    def save(self, user=None, commit=True):
        # Set author of the blog
        blog = super().save(commit=False)
        blog.author = user
        # also done is this way blog = Blog(title='title', des='des', content='content', author=user)

        if commit:
            blog.save()

        tags = self.cleaned_data.get('tags')
        if tags:
            tags = tags.split(',')
            for tag in tags:
                tag_obj, _ = Tag.objects.get_or_create(tag=tag.strip())
                tag_obj.blog.add(blog)

        return blog
    







    # for me

    # error giving Cannot assign "'testUser'": "Blog.author" must be a "User" instance.
    # This error usually occurs when you're trying to assign a value to a foreign key field that is not of the expected type. 
    # In this case, you're trying to assign a string to the author field, which is a foreign key to the User model.
    # To fix the error, you should pass a User instance as the value of the author field instead of a string. You can get the User instance by using the get_or_create method of the User model:
    # we have added a new field author_name to the form, which is used to get the username of the author. We then use the get_or_create method to get or create a User instance with the given username. 
    # Finally, we assign the User instance to the author field of the Blog instance before saving it.

