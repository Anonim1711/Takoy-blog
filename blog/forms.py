from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['author', 'date']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', 'blog', 'date']