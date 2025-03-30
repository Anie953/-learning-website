from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
