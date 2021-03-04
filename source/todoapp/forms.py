from django import forms
from django.forms import widgets

from .models import Task

class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    full_description = forms.CharField(max_length=3000, required=False, widget=widgets.Textarea, label='Полное описание')
    status = forms.ChoiceField(choices=Task.STATUS_CHOICES, required=True, label = 'Статус')
    date_completed = forms.DateField(required=False, label='Дата выполнения')
