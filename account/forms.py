from django import forms
from .models import Account , Transaction
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = (
            'username',
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = UserChangeForm.Meta.fields

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Account

class AddTransaction(forms.Form):
    type = forms.CharField()
    value = forms.FloatField()
    ps = forms.CharField(required=False)
    class Meta:
        model = Transaction
