from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
# Custom Signup Form with Registration Number
class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '---username---',
            'autocomplete': 'username',
            'aria-label': 'Username' 
            })
    )
    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'email'})
    )
    candidate_code = forms.CharField(
        label="",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Candidate code'})
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': ' password',
            'autocomplete': 'new-password',
            'aria-label': 'Password'
        }),
        required=True
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm  password',
            'autocomplete': 'new-password',
            'aria-label': 'Confirm Password'
        }),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'candidate_code', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            raise ValidationError("Passwords do not match.")
        return cleaned_data


# ✅ Custom Login Form (Username OR Registration Number)
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        max_length=150,
        required=False,  # Make optional since registration number can be used
        widget=forms.TextInput(attrs={'placeholder': 'username'})
    )
    candidate_code= forms.CharField(
        label="",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'candidate code'})
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'candidate_code', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        candidate_code = cleaned_data.get("candidate_code")

        if not username and not candidate_code:
            raise ValidationError("Please enter either your username or candidate code.")

        return cleaned_data


# ✅ Custom Forgot Password Form (Email OR Registration Number)
class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label="",
        max_length=254,
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'email'})
    )
    candidate_code = forms.CharField(
         label="",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Candidate code'})
    )

    class Meta:
        model = User
        fields = ['email', 'candidate_code']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        candidate_code = cleaned_data.get("candidate_code")

        if not email and not candidate_code:
            raise ValidationError("Please enter either your email or candidate code.")

        return cleaned_data

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
