from django import forms
from .models import *


class NameForm(forms.ModelForm):
    class Meta:
        model = Clients
        exclude = [""]
        fields = '__all__'

