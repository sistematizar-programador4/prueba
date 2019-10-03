from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets,status,generics
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SingleStudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProfessorListView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class SingleProfessorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ScoreListView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class SingleScoreView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class StudentView(viewsets.ViewSet):
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        student = get_object_or_404(student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def create(self, request):
        student = request.data.get('student')
        serializer = StudentSerializer(data=student)
        if serializer.is_valid(raise_exception=True):
            student_save = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def update(self, request,pk=None):
        student = request.data.get('student')
        model = get_object_or_404(Student,id=pk)
        serializer = StudentSerializer(model,data=student)
        if serializer.is_valid(raise_exception=True):
            student_save = serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request,pk=None):
        model = get_object_or_404(Student,id=pk)
        model.delete()
        return Response({"success": "Student '{}' deleted successfully".format(model.name)})

class ProfessorView(viewsets.ViewSet):
    def list(self, request):
        professor = Professor.objects.all()
        serializer = ProfessorSerializer(professor, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        professor = get_object_or_404(professor, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def create(self, request):
        professor = request.data.get('professor')
        serializer = ProfessorSerializer(data=professor)
        if serializer.is_valid(raise_exception=True):
            professor_save = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def update(self, request,pk=None):
        professor = request.data.get('professor')
        model = get_object_or_404(Professor,id=pk)
        serializer = ProfessorSerializer(model,data=professor)
        if serializer.is_valid(raise_exception=True):
            professor_save = serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request,pk=None):
        model = get_object_or_404(Professor,id=pk)
        model.delete()
        return Response({"success": "Professor '{}' deleted successfully".format(model.name)})

class ScoreView(viewsets.ViewSet):
    def list(self, request):
        score = Score.objects.all()
        serializer = ScoreSerializer(score, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        score = get_object_or_404(score, pk=pk)
        serializer = ScoreSerializer(score)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def create(self, request):
        score = request.data.get('score')
        serializer = ScoreSerializer(data=score)
        if serializer.is_valid(raise_exception=True):
            score_save = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def update(self, request,pk=None):
        score = request.data.get('score')
        model = get_object_or_404(Score,id=pk)
        serializer = ScoreSerializer(model,data=score)
        if serializer.is_valid(raise_exception=True):
            score_save = serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request,pk=None):
        model = get_object_or_404(Score,id=pk)
        model.delete()
        return Response({"success": "Professor '{}' deleted successfully".format(model.name)})