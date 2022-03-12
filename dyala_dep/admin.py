from atexit import register
from django.contrib import admin
from .models import Asol_ALdeen
# Register your models here.


class Studentadmin(admin.ModelAdmin):
    list_display = ['dName', 'dNumber', 'dDate', 'dTitle', 'dYear_grad','dDepartment','dImg']
    search_fields = ['dName', 'dNumber', 'dTitle']


admin.site.register(Asol_ALdeen, Studentadmin)
