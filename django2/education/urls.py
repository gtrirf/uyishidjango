from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('darsjadvali/', dars_jadvali, name='dars_jadvali'),
    path('teachers/', teachers_table, name='teacher'),
    path('students/', students_table, name='students'),
    path('groups/', groups_table, name='groups')
]
