from django.forms import ModelForm, TextInput, DateTimeInput
from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'due_on_date']

        widgets = {
            "task": TextInput(attrs={
                'placeholder': 'Your task',
                'type': 'text',
                'class': 'data-in'
            }),
            "due_on_date": DateTimeInput(attrs={
                'placeholder': 'Due on',
                'type': 'date',
                'class': 'data-in'
            })
        }
