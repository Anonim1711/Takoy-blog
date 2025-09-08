from django.db import models
from user.models import CustomUser

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    text = models.TextField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog.title}"
