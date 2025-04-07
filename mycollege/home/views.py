from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import SignupForm, LoginForm, ForgotPasswordForm

# Home View
def home(request):
    return render(request, 'home.html')

# Navbar View
def navbar(request):
    return render(request, 'navbar.html')

# About View
def about(request):
    return render(request, 'about.html')
def learn(request):
    return render(request, 'learn.html')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Signup failed. Please correct the errors.")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login View (Username OR Candidate Code)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            candidate_code = form.cleaned_data.get('candidate_code')
            password = form.cleaned_data.get('password')

            # Authenticate User
            user = None
            if username:
                user = authenticate(request, username=username, password=password)
            elif candidate_code:
                try:
                    user_obj = get_user_model().objects.get(candidate_code=candidate_code)
                    user = authenticate(request, username=user_obj.username, password=password)
                except get_user_model().DoesNotExist:
                    user = None

            if user:
                login(request, user)
                return redirect('details')
            else:
                messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

# Forgot Password View (Email OR Candidate Code)
def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            candidate_code = form.cleaned_data.get('candidate_code')

            try:
                if email:
                    user = get_user_model().objects.get(email=email)
                elif candidate_code:
                    user = get_user_model().objects.get(candidate_code=candidate_code)
                else:
                    user = None

                if user:
                    # Generate Password Reset Token
                    from django.contrib.auth.tokens import default_token_generator
                    from django.template.loader import render_to_string
                    from django.core.mail import send_mail

                    token = default_token_generator.make_token(user)
                    reset_link = request.build_absolute_uri(
                        f"/reset/{user.pk}/{token}/"
                    )
                    subject = "Password Reset Request"
                    message = f"Click the link below to reset your password:\n{reset_link}"
                    send_mail(subject, message, 'no-reply@example.com', [user.email])

                    messages.success(request, "Password reset email sent.")
                    return redirect('login')
                else:
                    messages.error(request, "User not found.")
            except get_user_model().DoesNotExist:
                messages.error(request, "User not found.")
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {'form': form})

# Protected Details View
@login_required
def details_view(request):    
    return render(request, 'details.html')
