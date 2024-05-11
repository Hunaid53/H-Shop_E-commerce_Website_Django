from django import forms
from .models import *

class Userform(forms.ModelForm):
    class Meta:
        model=Userregister
        fields='__all__'