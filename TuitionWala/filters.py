import django_filters
from .models import *
class EnrollmentFilter(django_filters.FilterSet):
    class meta:

        model = Enrollment
        fields = '__all__'


