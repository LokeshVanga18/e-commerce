from django import forms
from .models import *
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username' , 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        pas1 = cleaned_data.get('password')
        pas2 = cleaned_data.get('confirm_password')

        if pas1 != pas2:
            raise forms.ValidationError('Passwords Do Not Match')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile_number' , 'address']