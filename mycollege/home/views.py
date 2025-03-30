from django.shortcuts import render, redirect
from .forms import StudentSignupForm
from .models import Student

def signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
    else:
        form = StudentSignupForm()
    return render(request, 'signup.html', {'form': form})

def details(request):
    students = Student.objects.all()
    return render(request, 'details.html', {'students': students})
