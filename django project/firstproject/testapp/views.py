from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
def employee_info_view(request):
    employees= employee.objects.all()
    data={'employees': employees}
    res=render(request,'testapp/employees.html',data)
    return(res)
