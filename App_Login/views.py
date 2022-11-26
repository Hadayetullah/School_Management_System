from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

# Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Forms and Models
from App_Login.models import User, Profile
from App_Login.forms import SignUpForm, ProfileForm
from App_Teacher.models import Teacher
from App_Mark.models import Grade

# Messages
from django.contrib import messages

# Serializer
from .serializers import Students

# rest_framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

import datetime



# Create your views here.
def home(request):
    return render(request, 'App_Login/home.html', context={})



def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('App_Login:student_login'))
    return render(request, 'App_Login/sign_up.html', context={'form': form})


# Students -- (Default)
def login_user(request, user, value):
    # print("User Email: ", user)
    user_obj = User.objects.get(email=user)
    if value == "post":
        login(request, user_obj)
        # super_user = request.user
        # print(super_user)
        check_profile = Profile.objects.filter(user=user_obj, admitted=True)
        teacher = Teacher.objects.filter(user=user_obj)
        if user_obj.is_superuser == True:
            return HttpResponseRedirect(reverse("App_Login:admin_dashboard"))
        elif teacher.exists():
            return HttpResponseRedirect(reverse("App_Login:teacher_dashboard"))
        elif check_profile.exists():
            return HttpResponseRedirect(reverse("App_Login:dashboard"))
        else:
            return HttpResponseRedirect(reverse("App_Login:change_profile"))

    elif value == "logout":
        check_profile = Profile.objects.filter(user=user_obj)
        teacher = Teacher.objects.filter(user=user_obj)
        if user_obj.is_superuser == True:
            # teacher = Teacher.objects.filter(user=user_obj)
            # print(teacher)
            return HttpResponseRedirect(reverse("App_Login:admin_login"))
        elif teacher.exists():
            return HttpResponseRedirect(reverse("App_Login:teacher_login"))
        elif check_profile.exists():
            return HttpResponseRedirect(reverse("App_Login:student_login"))



def admin_login(request):
    # super_user = request.user
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                value = "post"
                if user.is_superuser == True:
                    user = user.email
                    return HttpResponseRedirect(reverse("App_Login:login", kwargs={"user":user, "value":value}))
                else:
                    messages.info(request, "Invalid Email or Password!")
                    return HttpResponseRedirect(reverse("App_Login:admin_login"))
    return render(request, 'App_Login/admin_login.html', context={'form': form})




def teacher_login(request):
    # super_user = request.user
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                value = "post"
                teacher = Teacher.objects.filter(user=user)
                # print(teacher)
                if teacher.exists():
                    user = teacher[0].user.email
                    return HttpResponseRedirect(reverse("App_Login:login", kwargs={"user":user, "value":value}))
                else:
                    messages.info(request, "Invalid Email or Password!")
                    return HttpResponseRedirect(reverse("App_Login:teacher_login"))
    return render(request, 'App_Login/teacher_login.html', context={'form': form})




def student_login(request):
    # super_user = request.user
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                value = "post"
                student = Profile.objects.filter(user=user)
                if student.exists():
                    user = student[0].user.email
                    # print(user)
                    return HttpResponseRedirect(reverse("App_Login:login", kwargs={"user":user, "value":value}))
                else:
                    messages.info(request, "Invalid Email or Password!")
                    return HttpResponseRedirect(reverse("App_Login:student_login"))
    return render(request, 'App_Login/student_login.html', context={'form': form})








@login_required
def logout_user(request):
    user = request.user.email
    value = "logout"
    logout(request)
    messages.warning(request, "You are logged out!")
    return HttpResponseRedirect(reverse("App_Login:login", kwargs={"user":user, "value":value}))


@login_required
def change_profile(request):
    session = datetime.datetime.today()
    session = session.year

    profile = Profile.objects.get(user=request.user)
    check_profile = Profile.objects.filter(user=request.user, admitted=True)
    super_user = request.user
    if super_user.is_superuser == True:
        return HttpResponseRedirect(reverse("App_Login:admin_dashboard"))
    elif super_user.is_staff == True:
        return HttpResponseRedirect(reverse("App_Login:teacher_dashboard"))
    # print(check_profile)
    # print(check_profile[0])
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile_obj = form.save(commit=False)

            profile_obj.session = session
            profile_obj.save()

            # class_no = form.cleaned_data['select_class']
            # full_name = form.cleaned_data['full_name']

            # grade = Grade.objects.get(user=request.user)[0]
            # grade.full_name = full_name
            # grade.class_no = class_no

            # grade.session = session
            # grade.save()

            if check_profile.exists():
                # print(check_profile[0].id)
                # messages.info(request, "Please complete your admission process!")
                messages.success(request, "Change Saved!!")
                # form = ProfileForm(instance=profile)
                return HttpResponseRedirect(reverse("App_Login:profile"))
            elif profile.is_fully_filled():
                return HttpResponseRedirect(reverse("App_Login:admission_fee"))
            else:
                messages.info(request, "Please fill up all the fields!")
                return HttpResponseRedirect(reverse("App_Login:change_profile"))
    return render(request, 'App_Login/change_profile.html', context={'form': form})


@login_required
def admission_fee(request):
    super_user = request.user
    if super_user.is_superuser == True:
        return HttpResponseRedirect(reverse("App_Login:admin_dashboard"))
    fee = Profile.objects.get(user=request.user, admitted=False)
    fee = fee.admission_fee()
    return render(request, 'App_Login/admission_fee.html', context={'fee': fee})


@login_required
def dashboard(request):
    check_profile = Profile.objects.filter(user=request.user, admitted=False)
    teacher = Teacher.objects.filter(user=request.user)
    super_user = request.user

    generate_roll = Profile.objects.filter(user=request.user, admitted=True, roll=0)
    if generate_roll:
        selected_class = generate_roll[0].select_class
        all_objects = Profile.objects.filter(select_class=selected_class, admitted=True)
        if all_objects:
            roll = len(all_objects)
            # grade = Grade.objects.filter(user=request.user)
            # grade.roll = roll
            # grade.save()
            
            generate_roll[0].roll = roll
            generate_roll[0].save()

    if super_user.is_superuser == True:
        return HttpResponseRedirect(reverse("App_Login:admin_dashboard"))
    elif teacher.exists():
        return HttpResponseRedirect(reverse("App_Login:teacher_dashboard"))
    elif check_profile.exists():
        if check_profile[0].is_fully_filled():
            return HttpResponseRedirect(reverse("App_Login:admission_fee"))
        else:
            messages.info(request, "Please fill up all the fields!")
            return HttpResponseRedirect(reverse("App_Login:change_profile"))
    return render(request, 'App_Login/dashboard.html', context={})


@login_required
def profile(request):
    teacher = Teacher.objects.filter(user=request.user, teacher=True)
    student = Profile.objects.filter(user=request.user, admitted=False)
    super_user = request.user
    if super_user.is_superuser == True:
        return HttpResponseRedirect(reverse("App_Login:admin_dashboard"))
    elif teacher.exists():
        return HttpResponseRedirect(reverse("App_Teacher:teacher_dashboard"))
    elif student.exists():
        messages.info(request, "You must fill up all the fields!")
        return HttpResponseRedirect(reverse("App_Login:change_profile"))
    return render(request, 'App_Login/profile.html', context={})




@login_required
def routine(request):
    return render(request, "App_Login/class_routine.html", context={})


# Rest Framework Views
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening



class StudentDetailAPIView(LoginRequiredMixin, APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, format=None):
        student_list = Profile.objects.filter(admitted=True)
        student_serializer = Students(student_list, many=True)
        return Response(student_serializer.data)









# Admin
@login_required
def admin_dashboard(request):
    super_user = request.user
    if super_user.is_superuser != True:
        return HttpResponseRedirect(reverse("App_Login:dashboard"))
    else:
        admin = 'admin'
    return render(request, 'App_Login/admin_dashboard.html', context={'admin': admin})


@login_required
def all_teacher(request):
    super_user = request.user
    if super_user.is_superuser != True:
        return HttpResponseRedirect(reverse("App_Login:dashboard"))
    else:
        admin = 'admin'
        search_teacher = 'EMPTY'

    teachers = Teacher.objects.filter(teacher=True)
    if teachers.exists():
        teachers = teachers

    if request.method == 'GET':
        add_teacher = request.GET.get('add_teacher', '')
        teacher_email = request.GET.get('teacher_email', '')
        teacher_id = request.GET.get('teacher_id', '')
        if add_teacher:
            result = User.objects.filter(email=add_teacher)
            # print('Add Teacher:', result)
            if result.exists():
                user = result[0]
                teacher = Teacher.objects.filter(user=user)
                if teacher:
                    messages.info(request, "The teacher already exists!")
                else:
                    user_obj = Teacher.objects.create(user=user)
                    # user_obj.user.is_staff = True
                    user_obj.id_no = 1000 + len(teachers)
                    user_obj.save()
                    # print('User Obj: ', user_obj.user)
                    return HttpResponseRedirect(reverse('App_Login:all_teacher'))
            else:
                messages.info(request, "The teacher does not exists. Please enter correct value!")
        elif teacher_email:
            search_value = User.objects.filter(email=teacher_email)
            if search_value.exists():
                search_value = search_value[0]
                result = Teacher.objects.filter(user=search_value, teacher=True)
                if result.exists():
                    search_teacher = result[0]
                    # if search_teacher:
                    #     search_teacher = search_teacher
                    # else:
                    #     search_teacher = 'EMPTY'
                else:
                    messages.info(request, "The teacher does not exists. Please enter correct email!")
            else:
                messages.info(request, "The teacher does not exists. Please enter correct email!")
        elif teacher_id:
            result = Teacher.objects.filter(id_no=teacher_id, teacher=True)
            if result.exists():
                search_teacher = result[0]
                # if search_teacher:
                #     search_teacher = search_teacher
                # else:
                #     search_teacher = 'EMPTY'
            else:
                messages.info(request, "The teacher does not exists. Please enter valid Id number!")
    return render(request, 'App_Login/all_teacher.html', context={'teachers': teachers, 'admin': admin, 'search_teacher': search_teacher})


def teacher_info(request, pk):
    teacher_key = User.objects.get(pk=pk)
    find_teacher = Teacher.objects.filter(user=teacher_key, teacher=True)
    # if request.user.is_superuser != True:
    #     return HttpResponseRedirect(reverse("App_Login:dashboard"))
    if request.user.is_superuser == True:
        if find_teacher.exists():
            if find_teacher[0].is_fully_filled():
                teacher = find_teacher[0]
                admin = "admin"
            else:
                return HttpResponseRedirect(reverse('App_Teacher:update_profile', kwargs={'pk':pk}))
    else:
        return HttpResponseRedirect(reverse("App_Login:logout"))

    return render(request, 'App_Teacher/teacher_info.html', context={'admin': admin, 'teacher': teacher})







import calendar

# Teacher
@login_required
def teacher_dashboard(request):
    days_list = list(calendar.day_name)

    teacher = Teacher.objects.filter(user=request.user)
    if teacher.exists():
        admin = "teacher"
        teacher = teacher[0]
    else:
        return HttpResponseRedirect(reverse("App_Login:logout"))
    return render(request, 'App_Login/admin_dashboard.html', 
    context={'admin': admin, 'teacher': teacher, 'days_list':days_list})
