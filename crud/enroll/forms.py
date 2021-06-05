from django import forms
from django.core.exceptions import ValidationError
from enroll.models import Student
from django.core import validators
from django.forms import widgets

class StudentRegistration(forms.ModelForm):
    class Meta:
       model = Student
       fields = ['name','email','password']
       widgets = {
           'name':forms.TextInput(attrs={'class':'form-control'}),
           'email':forms.TextInput(attrs={'class':'form-control'}),
           'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
       }
       


