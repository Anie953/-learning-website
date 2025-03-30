from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),    
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('signup/', views.signup_view, name='signup'),
    path('details/', views.details_view, name='details'),
]
