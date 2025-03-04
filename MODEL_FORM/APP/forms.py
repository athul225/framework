from django import forms
from .models import *

class model_forms(forms.ModelForm):
    class Meta:
        model=Student
        # fields=['roll','name','mark']
        fields='__all__'