from django import forms
from django.contrib.auth.models import User
from .models import EnrollmentForm_Table, Enrollment, Teaching_Form
import django_filters
from django.forms import ModelForm

class RegisterForm(forms.ModelForm):
    Mobile_No = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': None,
            'email': None,
        }

class Enrollment_Form(forms.ModelForm):
    class Meta:
        model = EnrollmentForm_Table
        fields = ('Username','Student_Name', 'Email', 'CourseID', 'Institute_Name', 'Mobile_No')

class TableForm(django_filters.FilterSet):
    class Meta:
        model = Enrollment
        fields = ('institute_names','fees','subjects')

class Entity_Form(forms.ModelForm):
    class Meta:
        model = Teaching_Form
        fields = '__all__'
        required = ('Entity_Name', 'Entity_Type','Address', 'City', 'State','Subjects', 'Average_Fee_Per_Subject')
        widgets = {
            'Address': forms.Textarea(attrs={"rows":2, "cols":30}),
            'Academic_Qualification_IF_Tutor':forms.TextInput(attrs={ 'required': 'true' }),
            'Years_Of_Establishment_IF_Institution':forms.TextInput(attrs={ 'required': 'true' }),
        }