from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),              # Displays list of all quizzes
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),  # Displays details of a specific quiz
    path('certificate/', views.certificate, name='certificate'), 
]
