from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from myapp.models import details

from .forms import CreateUserForm,LoginForm
from django.contrib.auth.decorators import login_required


# Authentication models and functions 

from django.contrib.auth.models import auth
from  django.contrib.auth import authenticate,login,logout

#for rest API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import myuser
from .serializer import UserSerializer



# Create your views here.
def name(request):
    template=loader.get_template('tempbutton.html')
    return HttpResponse(template.render())

def display(request):
    names = [
    {'name': 'anaswara', 'age': 21},
    {'name': 'abc', 'age': 24},
    {'name': 'efg', 'age': 26}
]
    context = {'names': names }
    template=loader.get_template('temp.html')
    return HttpResponse(template.render(context))

def students(request):
    students=details.objects.all().values()
    context={'students':students}
    template=loader.get_template('all_students.html')
    return HttpResponse(template.render(context))


def one_student(request,id):
    student=details.objects.get(id=id)
    context={'student':student}
    template=loader.get_template('one_student.html')
    return HttpResponse(template.render(context))

def std(request):
    student=student.objects.all().values()
    context={'student':student}
    template=loader.get_template('std.html')
    return HttpResponse(template.render(context))


def homepage(request):
    return render(request,'homepage.html')

def login(request):
    form = LoginForm()
    if request.method=='POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')

    context= {'loginform':form}        
    
    return render(request,'login.html',context)



def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'registerform':form}
    return render(request,'register.html',context=context)




@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

def user_logout(request):
    auth.logout(request)
    return redirect('homepage')


# api view

#to get users
@api_view(['GET'])
def get_user(request):
    context={'name': 'anu',
             'age': 21}
    return Response(UserSerializer(context).data)

# for get all user data in the database
@api_view(['GET'])
def get_users_db(request):
    users = myuser.objects.all()
    serialize = UserSerializer(users, many=True)
    return Response(serialize.data)

#to create new user using api
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


