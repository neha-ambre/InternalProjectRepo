from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages

from .models import UserCred


# Create your views here.

def fillForm(request):
    return render(request,'FormTemp.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            print('login successful')
            return redirect('fillForm')
        else:
            messages.info(request,'Username OR password is incorrect')
            # return render(request,'Login.html')
    return render(request,'Login.html')

def logout_user(request):
    logout(request)
    return render(request,'index.html')

def signUp(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
        
    context = {'form': form}
    return render(request,'SignUp.html',context)

def saveUser(request):
    username=request.POST.get('username')
    emailID=request.POST.get('email')
    contactNo=request.POST.get('contactNo')
    password=request.POST.get('password')
    # userCreds=UserCred(emailID=emailID,username=username,contactNo=contactNo, password=password)
    # userCreds.save()
    user_auth=authenticate(request,username=username,password=password)
    users=UserCred.objects.all()
    print(username,emailID,contactNo,password)
    return HttpResponse('User signed up')

def getUser(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    
    # users=UserCred.objects.all()
    # user_list=list(users)
    
    # print(username,emailID,contactNo,password)
    # flag=False
    # for user in user_list:
    #     if(username==user.username):
    #         flag=True
    #         break
    # if flag==True:
    #     return HttpResponse('User loged in')
    # else:
    #     return HttpResponse('Wrong Credentials')
    return HttpResponse('User loged in')
