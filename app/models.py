from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Score(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    student_id = models.ForeignKey(Student, related_name='students', on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, related_name='professors', on_delete=models.CASCADE)