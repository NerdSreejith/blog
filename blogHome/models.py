from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    content_in_short  = models.CharField(max_length=200, null=True)
    Full_content = RichTextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/images")

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog_parent = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = RichTextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog_parent.title}"

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_parent = models.ForeignKey(Comments, on_delete=models.CASCADE)
    reply = RichTextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.username} to {self.comment_parent.user.username}'s comment"
