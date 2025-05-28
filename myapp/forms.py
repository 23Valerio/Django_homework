from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)

    def clean(self): # type: ignore
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError("Incorrect username/password")
            
class RegistrerForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=("Password"), max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label=("Confirm Password"), max_length=100, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("username already used")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("passwords do not match")
        
        return cleaned_data