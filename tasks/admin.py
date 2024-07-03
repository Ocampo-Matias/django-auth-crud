from django.contrib import admin
from .models import task

class TasksAdmin(admin.ModelAdmin):
    readonly_fields=("created",)

# Register your models here.
admin.site.register(task,TasksAdmin)