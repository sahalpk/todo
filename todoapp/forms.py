from django.db.models.base import Model
from django.forms import fields
from .models import Task
from django import forms

class Todoform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']