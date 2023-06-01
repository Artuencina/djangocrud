from django.contrib import admin
from .models import Task

#Esto se pone para ver los campos de solo lectura en el panel
#de admin
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )
    
# Register your models here.
admin.site.register(Task, TaskAdmin)