from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

import datetime


from App_Login.models import Profile
from App_Mark.models import Grade
from App_Teacher.models import Teacher


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import SubmitGrade


from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from django.http import Http404


# Create your views here.
def grade(request):
    session = datetime.datetime.today()
    session = session.year

    teacher = Teacher.objects.filter(user=request.user)
    if teacher.exists():
        admin = "teacher"
        teacher = teacher[0]

    if request.method == 'GET':
        select_class = request.GET.get("select_class", "")
        select_course = request.GET.get("select_course", "")
        if select_class:
            if select_course:
                select_class = int(float(select_class))
                grade = Grade.objects.filter(class_no=select_class, subject=select_course, session=session)
                profile_obj_len = Profile.objects.filter(select_class=select_class, session=session, admitted=True)
                if profile_obj_len:
                    profile_len = len(profile_obj_len)
                    # print(profile_len)
                if grade.exists():
                    grade_len = len(grade)
                    if grade_len < profile_len:
                        for x in profile_obj_len:
                            individual_grade = Grade.objects.filter(
                            user=x.user,
                            class_no=select_class,
                            full_name=x.full_name,
                            subject=select_course,
                            roll=x.roll,
                            session=session
                            )
                            if individual_grade:
                                print(individual_grade)
                                pass
                            else:
                                grade_obj = Grade.objects.create(
                                user=x.user,
                                class_no=select_class,
                                full_name=x.full_name,
                                subject=select_course,
                                roll=x.roll,
                                session=session
                                )
                                grade_obj.save()
                        return HttpResponseRedirect(reverse('App_Mark:input_marks', kwargs={'class_no':select_class, 'subject':select_course}))
                    else:
                        return HttpResponseRedirect(reverse('App_Mark:input_marks', kwargs={'class_no':select_class, 'subject':select_course}))
                else:
                    # profile_obj_len = Profile.objects.filter(select_class=select_class, session=session, admitted=True)
                    for x in profile_obj_len:
                        grade_obj = Grade.objects.create(
                            user=x.user,
                            class_no=select_class,
                            full_name=x.full_name,
                            subject=select_course,
                            roll=x.roll,
                            session=session
                        )
                        grade_obj.save()
                    return HttpResponseRedirect(reverse('App_Mark:input_marks', kwargs={'class_no':select_class, 'subject':select_course}))
    return render(request, 'App_Mark/select_class.html', context={'admin':admin, 'teacher':teacher})



def input_marks(request, class_no, subject):
    session = datetime.datetime.today()
    session = session.year

    teacher = Teacher.objects.filter(user=request.user)
    if teacher.exists():
        admin = "teacher"
        teacher = teacher[0]
        
    grade = Grade.objects.filter(class_no=class_no, subject=subject, session=session)
    return render(request, 'App_Mark/input_marks.html', context={'admin':admin, 'teacher':teacher, 'grade':grade, 'class_no':class_no, 'subject':subject})



class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening



class StudentGrades(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = SubmitGrade


class StudentGrades1(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
      
    def put(self, request, user, format=None):
        all_data = request.data
        subject = all_data['subject']
        grade = Grade.objects.get(user=user, subject=subject)
        serializer = SubmitGrade(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        