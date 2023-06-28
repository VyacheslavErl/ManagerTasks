from django.forms import ModelForm, TextInput, DateInput, FileInput
from tasks.models import TaskModel

class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = ['name', 'text', 'do_before', 'image']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'text': TextInput(attrs={
                'class': 'form-control'
            }),
            'do_before': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'image': FileInput(attrs={
                'class': 'form-control'
            }),

        }



