from django.shortcuts import render,HttpResponse
from .models import Blog
from django.contrib.auth.models import  User
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,"index.html",{"blogs":blogs})


def content(request,pk):
    blogs = Blog.objects.get(pk = pk)
    return render(request,"content.html",{"blogs":blogs})

from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        # Assuming the form fields are named 'name', 'email', and 'password'
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Create a new user
        try:
            new_user = User.objects.create_user(username=email, email=email, password=password)
            # You can optionally set additional fields such as name
            new_user.first_name = name
            new_user.save()
            # Redirect to a success page or do something else
            return render(request, 'index.html')
        except Exception as e:
            # Handle any exceptions, such as a duplicate email
            return render(request, 'signup.html', {'error_message': str(e)})
    else:
        # Render the signup form template for GET requests
        return render(request, 'signup.html')
        
    return render(request,"signup.html")

def login(request):
    return render(request,'login.html')    