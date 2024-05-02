from django.contrib import admin
from .models import Members

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'joined_date')


admin.site.register(Members, MemberAdmin)


class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('path/to/custom.css',)
        }
