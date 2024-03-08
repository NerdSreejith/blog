from django.shortcuts import render,HttpResponse
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,"index.html",{"blogs":blogs})