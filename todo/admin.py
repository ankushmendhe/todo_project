from django.contrib import admin
from .models import ToDoItem

# Register your models here.
class ToDoItemAdmin(admin.ModelAdmin):
    list_display=['task_name','is_completed']


admin.site.register(ToDoItem,ToDoItemAdmin)
