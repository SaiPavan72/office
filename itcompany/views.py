"""
   app name itcompany and office project
"""

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from itcompany.forms import ApplicationForm, EmployeeForm
from itcompany.models import Application, Employee
from django.contrib import messages


def main(request):
    """ show login,application,register"""
    return render(request, 'itcompany/main.html')


def apply(request):
    """ show the application"""
    form = ApplicationForm
    return render(request, 'itcompany/application.html', {'form': form})


def save_application(request):
    """ save the application"""
    if request.method == 'POST':
        form_obj = ApplicationForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return render(request, 'itcompany/application.html', {'form': ApplicationForm(), 'error': form_obj.errors})

    return HttpResponseRedirect('/itcompany/')


def registration(request):
    """ registration form"""
    form = EmployeeForm
    return render(request, 'itcompany/registration.html', {'form': form})


def save_register(request):
    """ save the register details"""
    if Application.objects.filter(email=request.POST['email'], is_verified=True).exists():
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                        email=request.POST['email'])
        office = Application.objects.get(email=request.POST["email"])
        Employee.objects.create(phone=request.POST['phone'], image=request.FILES['image'],
                                salary=request.POST['salary'], email=request.POST['email'], user=user, office=office)
        return HttpResponseRedirect('/itcompany/')
    else:
        return render(request, 'itcompany/application.html', {'error': 'you are not eigible for this job'})

def login_user(request):
    return render(request, 'itcompany/login.html')

def login_request(request):
    """ login the employee"""
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if Employee.objects.filter(user=user).exists():
            return HttpResponseRedirect('/itcompany/details/')
        else:
            return render(request, 'itcompany/login.html', {'error': 'Invalid username or password'})

    else:
        return render(request, 'itcompany/login.html', {'error': 'Invalid username or password'})

def employee_details(request):
    """ show the employee details"""
    user = request.user
    gmail = user.email
    print(gmail)
    data = Employee.objects.get(email=gmail)
    x = data.office.designation
    print(x)
    print(type(x))
    if x == 'CEO':


        return render(request, 'itcompany/permission.html', {'user': user, 'data': data})
    else:

        return render(request, 'itcompany/details.html', {'form': data, 'user': user})



def application_permission(request):
    data = Application.objects.filter(is_verified=False)



    return render(request, 'itcompany/accept.html', {'data': data})


def applied_details(request,id):
    data = Application.objects.get(id=id)
    return render(request, 'itcompany/applied.html', {'data': data})
