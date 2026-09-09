from django.contrib import admin
from todo.models import Task
# Register your models here.


class todo (admin.ModelAdmin):
    list_display=( 'task' , 'status' , 'created_date' )

admin.site.register(Task,todo)