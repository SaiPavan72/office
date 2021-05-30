"""
   app name itcompany and office project
"""

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from itcompany.forms import ApplicationForm, EmployeeForm, GmailForm, ProjectForm, TeamForm
from itcompany.models import Application, Employee, Project, Team

from django.conf import settings


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
    """ enter the user credencials"""
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
    print(x.role)
    print(type(x.role))

    y = 1
    emp = False
    if x.role == 'CEO' or 'HR':
        emp = True

    return render(request, 'itcompany/permission.html', {'data': data, 'user': user, 'emp': emp})


def application_permission(request):
    """ show the data to the credencials"""
    data = Application.objects.filter(is_verified=False)

    return render(request, 'itcompany/accept.html', {'data': data})


def applied_details(request, id):
    """ show the applied details"""
    data = Application.objects.get(id=id)
    return render(request, 'itcompany/applied.html', {'data': data})


def total_teams(request):
    """ total teams list """
    data = Team.objects.all()
    import pdb
    # pdb.set_trace()
    return render(request, 'itcompany/total_team.html', {'data': data})


def team(request):
    """ for  creating teams """
    form = TeamForm
    return render(request, 'itcompany/team.html', {'form': form})


def save_team(request):
    """ saving team """
    if request.method == 'POST':
        form_obj = TeamForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return HttpResponseRedirect('/itcompany/total_teams/')

    return HttpResponseRedirect('/itcompany/total_teams/')


def total_projects(request):
    """ total projects """
    data = Project.objects.all()

    return render(request, 'itcompany/project_list.html', {'data': data})


def project(request):
    """ creating project """
    form = ProjectForm()
    return render(request, 'itcompany/project.html', {'form': form})


def save_project(request):
    """ saving project-"""
    if request.method == 'POST':
        form_obj = ProjectForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return HttpResponseRedirect('/itcompany/total_projects/')


def logout_page(request):
    """ logout page"""
    logout(request)
    return HttpResponseRedirect('/itcompany/login_page/')


def sent_mail(request):
    """ send mail"""
    data = Employee.objects.all()

    form = GmailForm

    return render(request, 'itcompany/email.html', {'form': form, 'mail': data})


def save_mail(request):
    """ saved mails"""
    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = request.POST.get('message')
        reciever = request.POST.get('email')
        send_mail(subject, body, settings.EMAIL_HOST_USER,
                  [reciever], fail_silently=False)
        return render(request, 'itcompany/mail_sent.html', {'email': reciever})

    return render(request, 'itcompany/main.html', {})


def employ_list(request):
    """ show the employ list """
    data = Employee.objects.all()
    return render(request, 'itcompany/emp_list.html', {'data': data})


def emp_details(request, id):
    """ show the emp details"""
    data = Employee.objects.get(id=id)
    return render(request, 'itcompany/emp_details.html', {'data': data})
