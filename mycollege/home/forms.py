from django import forms
from .models import Student

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']
