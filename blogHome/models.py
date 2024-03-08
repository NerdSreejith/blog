from django.db import models

# Create your models here.
class Blog(models.Model):
    Name = models.CharField(max_length=50,null=True)
    title = models.CharField(max_length=100,null = True)
    s_content = models.CharField(max_length=200,null=True)
    content=models.TextField()
    time = models.TimeField(auto_now_add=True) 
    image =models.ImageField(upload_to="blog/images")