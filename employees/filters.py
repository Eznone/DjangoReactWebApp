import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    id = django_filters.RangeFilter(field_name='id')
    # Note that filter_by_id_range is a custom filtter utilizing a function
    emp_id_min = django_filters.CharFilter(field_name='filter_by_id_range', label="From EMP ID")
    emp_id_max = django_filters.CharFilter(field_name='filter_by_id_range', label="To EMP ID")


    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id', 'emp_id_min', 'emp_id_max']

    # queryset comes from FilterSet in class EmployeeFilter parameter
    def filter_by_id_range(self, queryset, name, value):
        if name == "emp_id_min":
            return queryset.filter(emp_id__gte=value)
        elif name == "emp_id_max":
            return queryset.filter(emp_id__lte=value)
        return queryset