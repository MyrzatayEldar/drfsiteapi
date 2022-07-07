from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('boss', )  # Убрал это поле, из-за того что при загрузке устройство начинает зависать

