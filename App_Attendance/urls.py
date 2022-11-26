from django.urls import path
from App_Attendance.views import attendance, take_attendance, view_attendance, StudentAPIView #, TakeAttendanceAPIView
from django.views.decorators.csrf import csrf_exempt

app_name = 'App_Attendance'


urlpatterns = [
    path('', attendance, name='attendance'),
    path('take_attendance/<class_no>/', take_attendance, name='take_attendance'),
    path('view_attendance/<date>/<class_no>/', view_attendance, name='view_attendance'),
    # path('studentdata/', csrf_exempt(TakeAttendanceAPIView.as_view())),
    path('api/', StudentAPIView.as_view()),
]
