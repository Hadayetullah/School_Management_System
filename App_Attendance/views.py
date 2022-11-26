from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib import messages


# from App_Attendance.forms import AttendanceForm
from App_Login.models import Profile, User
from App_Teacher.models import Teacher
from .models import Attendance
from .serializers import StudentSerializer, TakeAttendance



from rest_framework.authentication import SessionAuthentication, BasicAuthentication


from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response

from datetime import datetime




# Create your views here.
@login_required
def attendance(request):
    teacher = Teacher.objects.filter(user=request.user)
    if teacher.exists():
        teacher = teacher[0]
        # print(teacher.surname)
        admin = "teacher"
        if request.method == 'GET':
            class_field = request.GET.get("class_field", "")
            date_field = request.GET.get("date_field", "")
            another_class_field = request.GET.get("another_class_field", "")

            if class_field:
                class_field = int(class_field)
                # print(type(class_field))
                return HttpResponseRedirect(reverse("App_Attendance:take_attendance", kwargs={'class_no':class_field}))
            elif date_field:
                p = date_field.split("-")
                arr = []
                for i in p:
                    arr.append(i.lstrip("0"))
                x, y, z = arr
                # y = int(y) - 1
                # q = z + str(y) + x
                q = y + z + x
                # print(q)
                selected_date = datetime.strptime(q, "%m%d%Y").date()
                # print("Date",selected_date)
                # print(selected_date, another_class_field)

                class_no = int(another_class_field)
                # student = Attendance.objects.filter(class_no=class_no, created="2022-09-07")
                student = Attendance.objects.filter(class_no=class_no, created=selected_date)
                # print(student)
                if student.exists():
                    return HttpResponseRedirect(reverse("App_Attendance:view_attendance", kwargs={'date':selected_date, 'class_no':class_no}))
                else:
                    messages.info(request, "Attendance does not exist of the date")
                    return HttpResponseRedirect(reverse("App_Attendance:attendance"))
    else:
        return HttpResponseRedirect(reverse("App_Login:logout"))
    return render(request, 'App_Attendance/attendance_detail.html', context={'admin':admin, 'teacher':teacher})




@login_required
def take_attendance(request, class_no):
    teacher = Teacher.objects.filter(user=request.user)
    if teacher.exists():
        teacher = teacher[0]
        admin = "teacher"
        students = Profile.objects.filter(select_class=class_no, admitted=True)
    else:
        return HttpResponseRedirect(reverse("App_Login:logout"))
    return render(request, 'App_Attendance/attendance.html', 
    context={'students':students, 'class_no':class_no, 'admin':admin, 'teacher':teacher})



@login_required
def view_attendance(request, date, class_no):
    # print(date, class_no)
    teacher = Teacher.objects.filter(user=request.user)
    if teacher.exists():
        admin = "teacher"
        teacher = teacher[0]
        students = Profile.objects.filter(select_class=class_no, admitted=True)
    else:
        return HttpResponseRedirect(reverse("App_Login:logout"))
    return render(request, 'App_Attendance/view_attendance.html', 
    context={'admin':admin, 'teacher':teacher, 'students':students, 'class_no':class_no, 'date':date})



class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening





class StudentAPIView(LoginRequiredMixin, APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, format=None):
        student_list = Attendance.objects.all()
        student_serializer = TakeAttendance(student_list, many=True)
        return Response(student_serializer.data)
            
    def post(self, request, format=None):
        teacher_id = Teacher.objects.filter(user=request.user, teacher=True)
        all_data = request.data
        all_data['user'] = teacher_id[0].id
        # all_data['created'] = datetime.date.today()
        #  all_data['created'] = datetime.date(2022, 9, 15)

        # created = str(datetime(2020, 6, 15, 11, 00, tzinfo=UTC))
        # all_data['created'] = created

        # print("All Data: ", all_data)
        serializer = TakeAttendance(data=all_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
