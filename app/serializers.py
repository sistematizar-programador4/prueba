from rest_framework import serializers
from django.forms import widgets
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name')

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'name')

class ScoreSerializer(serializers.ModelSerializer):
    professor = serializers.PrimaryKeyRelatedField(many=False,read_only=True)
    student = serializers.PrimaryKeyRelatedField(many=False,read_only=True)
    class Meta:
        model = Score
        fields = ('id', 'name', 'value', 'student_id', 'professor_id','professor','student')
