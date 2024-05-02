from django.shortcuts import render
from django.template import loader
from .models import *
from django.http import HttpResponse
# Create your views here.


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def dars_jadvali(request):
    jadval = Darsjadvali.objects.all()
    template = loader.get_template('darsjadvali.html')
    context = {
        'jadval': jadval
    }
    return HttpResponse(template.render(context, request))


def teachers_table(request):
    teachers = Teachers.objects.all()
    template = loader.get_template('teachers.html')
    context = {
        'teachers': teachers
    }
    return HttpResponse(template.render(context, request))


def students_table(request):
    students = Students.objects.all()
    template = loader.get_template('students.html')
    context = {
        'students': students
    }
    return HttpResponse(template.render(context, request))


def groups_table(request):
    groups = Groups.objects.all()
    template = loader.get_template('groups.html')
    context = {
        'groups': groups
    }
    return HttpResponse(template.render(context, request))
