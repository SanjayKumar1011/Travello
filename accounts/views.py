from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse


# Create your views here.
def register(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        print(name)
        print(email)
        print(password)

        if password != confirm_password:
            messages.error(request,"Password not match")
            return redirect("register")
        elif User.objects.filter(username=name).exists():
            messages.error(request,"username already exists")
            return redirect("register")
        
        user=User.objects.create_user(username=name,email=email,password=password)
        user.save()
        print(user)
        return redirect('login')
       


    return render(request,'register.html')

def loginUser(request):
    if request.method=='POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        authenticated_user = authenticate(request, username=name, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user) 
            messages.success(request, "Registration successful. You are now logged in!")
            return redirect('/')
        else:
            messages.error(request, "Authentication failed.")
            return redirect('login')
    
    return render(request,'login.html')
    
def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def JWTcredsofUser(request):
    if request.method=='POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        authenticated_user = authenticate(request, username=name, password=password)

        if authenticated_user is not None:
            refresh = RefreshToken.for_user(authenticated_user)
            return JsonResponse({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': authenticated_user.username
            })
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
    return render(request,'login.html')