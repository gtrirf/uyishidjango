from django.contrib import admin
from .models import Darsjadvali, Students, Groups, Weekdays, Teachers

# Register your models here.

@admin.register(Darsjadvali)
class DarsjadvaliAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'group_id', 'weekday_id')

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    pass

@admin.register(Weekdays)
class WeekdaysAdmin(admin.ModelAdmin):
    pass

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    pass
