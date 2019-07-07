from django import forms
from .models import Customer
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        clean_all = super().clean()
        pass1 = clean_all['password']
        pass2 = clean_all['password2']
        if pass1 != pass2:
            raise forms.ValidationError('the password is not the same')


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['address']

