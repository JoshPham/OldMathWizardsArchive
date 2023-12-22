from . import views
from .views import GradeView, UnitView, LessonView, ProblemView
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('grade/', GradeView.as_view(), name="grade"),
    path('unit/', UnitView.as_view(), name="unit"),
    path('lesson/', LessonView.as_view(), name="lesson"),
    path('problem/', ProblemView.as_view(), name="problem"),
]