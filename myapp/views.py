from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect




# Create your views here.
@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        resp = {"message":"Login successfully.", "status":"SUCCESS"}
        return Response(resp, status=200)
    else:
        resp = {"message": "Login failed.", "status":"FAIL"}
        return Response(resp)

@api_view(['POST'])
def signup(request):
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    resp = {"message": "signup successfully.", "status":"SUCCESS"}
    return Response(resp)

@api_view(['POST'])
def logout(request):
    logout(request)
    resp = {"message": "Logout successfully."}
    return Response(resp, status=200)

def loginPage(request):
    # if (request.user):
    #     return redirect('/home')
    return render(request, 'login.html')

def signupPage(request):
    # if (request.user):
    #     return redirect('/home')
    return render(request, 'signup.html')

@login_required
def home(request):
    return render(request, 'home.html')

