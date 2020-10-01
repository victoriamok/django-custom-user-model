from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.forms import ModelForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=30, label='E-mail', help_text='Enter a valid e-mail address')
    first_name = forms.CharField(max_length=30, help_text='Enter a name')
    last_name = forms.CharField(max_length=30, help_text='Enter a surname')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',)


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")


class UserAccountUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        try:
            CustomUser.objects.exclude(pk=self.instance.pk).get(first_name=first_name)
        except ObjectDoesNotExist:
            return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['first_name']
        try:
            CustomUser.objects.exclude(pk=self.instance.pk).get(last_name=last_name)
        except ObjectDoesNotExist:
            return last_name


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class RemoveUser(forms.Form):
    email = forms.CharField()

