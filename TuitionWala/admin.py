from django.contrib import admin
from .models import Faculty
from .models import Users
from .models import MyStudent
from .models import Enrollment, EnrollmentForm_Table, Teaching_Form
# Register your models here.
admin.site.register(MyStudent)
admin.site.register(Faculty)
admin.site.register(Users)
admin.site.register(Enrollment)
admin.site.register(EnrollmentForm_Table)
admin.site.register(Teaching_Form)