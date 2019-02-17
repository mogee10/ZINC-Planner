from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'password']
        widgets = {
        	'password': forms.PasswordInput(),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    fields = ['username', 'password']
    widgets = {
        	'password': forms.PasswordInput(),
        }


<<<<<<< HEAD
=======

class UserLoginForm(forms.Form):
	

class EventForm(forms.ModelForm):
	class Meta:
>>>>>>> 99f9a3df552a9772b3e0de29d75c0f4f1f9540e4
