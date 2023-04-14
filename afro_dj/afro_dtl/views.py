from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import User_account
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    pr_title = 'Afro-Django'
    username = 'Olive'
    gender = 'Female'
    return render(
        request, 
        'index.html', 
        {'pr_title': pr_title, 'username':username, 'gender':gender}
        )

def register(request):
    return render(request, 'register.html')

def registration(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    user_details=[
            username,email,password,gender
        ]
    print(user_details)
    if User.objects.filter(username=user_name).first():
        print('username already exists.')
        return render(request, 'index.html')
    else:
        user=User.objects.create_user(user_name, email,password)
        return render(request, 'login.html')
    
   

