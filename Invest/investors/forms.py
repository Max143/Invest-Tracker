from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Investment, Investor


class InvestorsForm(forms.ModelForm):

    class Meta :
        model = Investment
        fields = ['amount', 'rate', 'investor']




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
