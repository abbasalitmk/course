from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'input100 border-start-0 form-control ms-0', 'placeholder': 'Email'}),

    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input100 border-start-0 form-control ms-0', 'placeholder': 'Password'}),
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email',]


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input100 form-control', 'placeholder': 'Current Password'})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input100 form-control', 'placeholder': 'New Password'})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input100 form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
