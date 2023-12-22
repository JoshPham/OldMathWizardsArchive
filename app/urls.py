from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('grade/', get_grades, name="grade"),
    path('unit/', UnitView.as_view(), name="unit"),
    path('lesson/', LessonView.as_view(), name="lesson"),
    path('problem/', ProblemView.as_view(), name="problem"),
]