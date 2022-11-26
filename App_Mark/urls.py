from django.urls import path
from .views import grade, input_marks, StudentGrades, StudentGrades1

app_name = 'App_Mark'


urlpatterns = [
    path('', grade, name='grade'),
    path('input_marks/<int:class_no>/<str:subject>/', input_marks, name='input_marks'),
    path('gradeApi/', StudentGrades.as_view()),
    path('gradeApi1/<user>/', StudentGrades1.as_view()),
]