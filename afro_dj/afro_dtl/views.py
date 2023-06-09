from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import User_account, About_form
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    pr_title = 'Afro-Django'
    
    if request.user.is_authenticated:
        username = request.user.username 
        
        return render(
        request, 
        'index.html', 
        {'pr_title': pr_title, 'username':username}
        )
    
    else:
        author = 'Olive'
        gender = 'Female'
        return render(
        request, 
        'index.html', 
        {'pr_title': pr_title, 'author':author, 'gender':gender}
        )
     

def register(request):
    return render(request, 'register.html')

def registration(request):
    user_name = request.POST['username']
    email = request.POST['user_email']
    password = request.POST['password']
    gender = request.POST['gender']
    user_details=[
            user_name, email,password,gender
        ]
    print(user_details)
    if User.objects.filter(username=user_name).first():
        print('username already exists.')
        return render(request, 'login.html')
    else:
        user=User.objects.create_user(user_name, email,password)
        return render(request, 'login.html')

def login_user(request):
    user_name = request.POST['username']
    pwd = request.POST['password']
    if User.objects.filter(username=user_name).first():
        print('This username exists')
        logged_user = authenticate(request, username=user_name, password=pwd)
        if logged_user is not None:
            #here we are logging in the user
            auth_login(request,logged_user)
            print(user_name+" " + "logged in successfully")
            return redirect('index')
        else:
            #here we are handling a scenario where the authentication has failed
            #here we then redirect them back to the login page
            return render(request, 'login.html')
    else:
        print("user credentials do not exist")
        return render(request, 'login.html')
    
def login_page(request):
    return render(request, 'login.html')


@login_required
def logout_user(request):
    auth_logout(request)
    return redirect('login_page')

def about_form(request):
    
    user_name = request.POST['username']
    email = request.POST['user_email']
    gender = request.POST['gender']
    university = request.POST['user_university']
    course = request.POST['user_course']
    cohort = request.POST['user_cohort']

    user_details=[user_name,email,gender,university,course,cohort] 
    
    return render(request, 'display.html', {'user_details':user_details,})

def about(request):
    return render(request, 'about.html')



