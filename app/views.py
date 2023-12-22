from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializer import * 

def home(request):
    return render(request, "home.html")

class GradeView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    def get(self, request):
        output = [{"grade_id": output.grade_id, 
                   "title": output.title, 
                   "description": output.description, 
                   "units": output.units}
                  for output in Grade.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class UnitView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    def get(self, request):
        output = [{"grade": output.grade, 
                   "unit_id": output.unit_id, 
                   "title": output.title, 
                   "description": output.description, 
                   "lessons": output.lessons}
                  for output in Unit.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class LessonView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    def get(self, request):
        output = [{"unit": output.unit, 
                   "lesson_id": output.lesson_id, 
                   "title": output.title, 
                   "description": output.description, 
                   "content": output.content, 
                   "problems": output.problems}
                  for output in Lesson.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class ProblemView(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    def get(self, request):
        output = [{"lesson": output.lesson, 
                   "text_question": output.text_question, 
                   "num_answer": output.num_answer, 
                   "answer_a": output.answer_a, 
                   "answer_b": output.answer_b, 
                   "answer_c": output.answer_c, 
                   "answer_d": output.answer_d}
                  for output in Problem.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)