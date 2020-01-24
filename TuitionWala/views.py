import pickle
from django.shortcuts import render, redirect
from TuitionWala.forms import RegisterForm
#from TuitionWala.forms import Users
# Create your views here.
from django.http import HttpResponse
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import EnrollmentFilter
from .models import Enrollment, EnrollmentForm_Table
from .forms import Enrollment_Form, TableForm, Entity_Form
from django.contrib import messages
# Create View Here
def index(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'index.html', context=my_dict)

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('TuitionWala:index'))


def RegistrationForm(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            user = form.save(commit=True)
            # Hash the password
            user.set_password(user.password)
            user.save()
            form = RegisterForm()
        else:
            print("FORM IS INVALID PLEASE REGISTER AGAIN !")

    return render(request, 'register.html', {'form': form})

def about(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'about.html', context=my_dict)

def login_page(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'login.html', context=my_dict)

def contact(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'contact.html', context=my_dict)

def main_page(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'main.html', context=my_dict)

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(request,username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('TuitionWala:main_page'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, 'The login details you entered are invalid. Please try again.')
            return render(request, 'login.html')

    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {})

def fburl(request):
    return redirect("https://www.facebook.com/umang.rana.39")

def partner_institutions(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'Partner_Institutions.html', context=my_dict)

def inst1(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst1.html', context=my_dict)

def inst2(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst2.html', context=my_dict)

def inst3(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst3.html', context=my_dict)

def inst4(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst4.html', context=my_dict)

def inst5(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst5.html', context=my_dict)

def inst6(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst6.html', context=my_dict)

def inst7(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst7.html', context=my_dict)

def inst8(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst8.html', context=my_dict)

def inst9(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst9.html', context=my_dict)

def inst10(request):
    my_dict = {'insert_me': "Hello Iam from Views.py !"}
    return render(request, 'insts/inst10.html', context=my_dict)

def table(request):
    EnrollmentData = Enrollment.objects.all()
    context = {'Enrollment_Data': EnrollmentData,}
    return render(request, 'table.html', context)

def filtering(request):
    myFilter = EnrollmentFilter(request.GET,queryset=Enrollment.objects.all())
    context = {'myFilter': myFilter}
    return render(request, 'table.html', context)

def EnrollmentForm(request):
    EnrollmentForm = Enrollment_Form()

    if request.method == 'POST':
        EnrollmentForm = Enrollment_Form(data=request.POST)

        if EnrollmentForm.is_valid():
            user = EnrollmentForm.save(commit=True)
            # Hash the password

            user.save()
            EnrollmentForm = Enrollment_Form()
        else:
            print("FORM IS INVALID PLEASE REGISTER AGAIN !")

    return render(request, 'EnrollmentForm.html', {'EnrollmentForm': EnrollmentForm})

def tablew(request):
    EnrollmentData = Enrollment.objects.all()
    context = {'Enrollment_Data': EnrollmentData, }
    return render(request, 'tablew.html', context)


def status(request):
    print(request.user.username)
    Form_Data = EnrollmentForm_Table.objects.all().filter(Username=request.user.username)
    context = {'Form_Data': Form_Data}
    return render(request, 'status.html', context)

def status_table(request):
    Form_Data = EnrollmentForm_Table.objects.all()
    context={'endata': Form_Data}
    return render(request, 'status.html', context)

def Entity_Registration_Form(request):
    EntityForm = Entity_Form()

    if request.method == 'POST':
        EntityForm = Entity_Form(data=request.POST)

        if EntityForm.is_valid():
            user = EntityForm.save(commit=True)
            # Hash the password
            EntityForm = Entity_Form()
        else:
            print("FORM IS INVALID PLEASE REGISTER AGAIN !")

    return render(request, 'Register_Entity.html', {'EntityForm': EntityForm})
