from django import forms
from .models import ToDoItem

class ToDoItemForm(forms.ModelForm):
    class Meta:
        model=ToDoItem
        fields=['task_name','is_completed']

