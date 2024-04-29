from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from .models import Blog,Comments
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def home(request):
    blogs = Blog.objects.all()
    return render(request,"index.html",{"blogs":blogs})


def content(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comments.objects.filter(blog_parent=blog)
    return render(request, "content.html", {"blogs": blog, "comments": comments})

from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            new_user = User.objects.create_user(username=email, email=email, password=password)
            new_user.first_name = name
            new_user.save()
            messages.success(request, 'User created successfully. You are now logged in.')
            return render(request, 'index.html')
        except Exception as e:
            
            return render(request, 'signup.html', {'error_message': str(e)})
    else:
        
        return render(request, 'signup.html')
        
    return render(request,"signup.html")



def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome!!!!')
            return redirect('home')
        else:
            print("Invalid credentials")
    
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('home')

@login_required
def comment(request):
    if request.method == "POST":
        user = request.user  # Get the currently logged-in user
        blog_comment = request.POST.get("comment")
        blog_id = request.POST.get("blog_id")
        blog = Blog.objects.get(pk=blog_id)
        comment = Comments(user=user, blog_parent=blog, comment=blog_comment)
        comment.save()
        messages.success(request, "Comment added")

        return redirect(reverse('content', kwargs={'pk': blog_id}))
    else:
        return redirect('login')

from .forms import BlogForm  # Import your BlogForm from forms.py
@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, "Blog created successfully")
            return redirect('home')
        else:
            messages.error(request, "Blog creation failed. Please check the form.")
    else:
        form = BlogForm()
    return render(request, 'create.html', {'form': form})
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'create.html', {'form': form, 'blog': blog})



def  delete_blog(request,blog_id):
    instance = Blog.objects.get(pk=blog_id)
    instance.delete()
    return redirect('home')