from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'post', 'hiring_date', 'salary', )
    list_filter = ('hiring_date', )
    search_fields = ('fullname', 'post', 'hiring_date', 'salary', ) #поля, по которым идет поиск


class BossAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'hiring_date', 'salary', )
    list_filter = ('hiring_date',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Boss, BossAdmin)
