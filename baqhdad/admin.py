from django.contrib import admin

# Register your models here.
from .models import *


class Studentadmin(admin.ModelAdmin):
    list_display = ['dName', 'dNumber', 'dDate',
                    'dTitle', 'dYear_grad', 'dDepartment', 'dImg']
    search_fields = ['dName', 'dNumber', 'dTitle']


admin.site.register(Asol_ALdeen_Boys, Studentadmin)

admin.site.register(Asol_ALdeen_Girls, Studentadmin)

admin.site.register(English, Studentadmin)

admin.site.register(FiqhFound, Studentadmin)


admin.site.register(ArabicLan, Studentadmin)

admin.site.register(History, Studentadmin)


admin.site.register(Law, Studentadmin)

admin.site.register(FinanceBanking, Studentadmin)
