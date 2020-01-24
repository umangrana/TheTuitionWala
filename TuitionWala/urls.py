from django.urls import path
from django_filters.views import FilterView

from . import views
from .filters import EnrollmentFilter

app_name = 'TuitionWala'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.RegistrationForm),
    path('about', views.about),
    path('user_login', views.user_login, name='user_login'),
    path('contact', views.contact),
    path('main_page', views.main_page, name='main_page'),
    path('partner_institutions', views.partner_institutions, name='partner_institutions'),
    path('inst1', views.inst1),
    path('inst2', views.inst2),
    path('inst3', views.inst3),
    path('inst4', views.inst4),
    path('inst5', views.inst5),
    path('inst6', views.inst6),
    path('inst7', views.inst7),
    path('inst8', views.inst8),
    path('inst9', views.inst9),
    path('inst10', views.inst10),
    path('fburl', views.fburl),
    path('enrollment_console', views.table),
    path('enrollment_form', views.EnrollmentForm),
    path('enrollment_consoled', views.tablew),
    path('status', views.status),
    path('Entity_Registration_Form', views.Entity_Registration_Form)
]