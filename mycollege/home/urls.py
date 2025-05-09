from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('navbar/', views.navbar, name='navbar'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),    
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('signup/', views.signup_view, name='signup'),
    path('details/', views.details_view, name='details'),
    path('learn/', views.learn, name='learn'),
    path('contact/', views.contact_view, name='contact'),
]
