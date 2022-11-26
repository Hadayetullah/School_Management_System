from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


# Authentication
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Forms and Models
from App_Login.models import User

from App_Teacher.forms import TeacherForm
from App_Teacher.models import Teacher


# Messages
from django.contrib import messages


# Create your views here.
@login_required
def change_teacher_prof(request, pk):
    teacher_key = User.objects.get(pk=pk)
    new_teacher = Teacher.objects.filter(user=teacher_key, teacher=True)
    teacher = Teacher.objects.filter(user=request.user, teacher=True)

    is_teacher = False
    if request.user.is_superuser == True:
        admin = 'admin'
        if new_teacher.exists():
            teacher = new_teacher[0]
            is_teacher = True
        else:
            return HttpResponseRedirect(reverse('App_Login:admin_dashboard'))

    elif teacher.exists():
        admin = 'teacher'
        teacher = teacher[0]
    # if request.user.is_superuser != True or request.user.is_staff != True:
    else:
        return HttpResponseRedirect(reverse("App_Login:dashboard"))

    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            user_obj = form.save()
            # user_obj.user = request.user
            # user_obj.save()
            form = TeacherForm(instance=teacher)
            messages.success(request, "Profile Saved")
            if is_teacher == True:
                if new_teacher[0].is_fully_filled():
                    return HttpResponseRedirect(reverse('App_Login:teacher_info', kwargs={'pk':pk}))
                if not new_teacher[0].is_fully_filled():
                    messages.info(request, "Please fill up all the fields or the teacher must fill up all the fields!")
                    return HttpResponseRedirect(reverse('App_Login:all_teacher'))
            else:
                return HttpResponseRedirect(reverse('App_Teacher:teacher_profile'))
    return render(request, 'App_Teacher/teacher_form.html', context={'form': form, 'admin': admin, 'teacher':teacher})


@login_required
def teacher_profile(request):
    teacher = Teacher.objects.filter(user=request.user, teacher=True)
    if request.user.is_superuser == True:
        admin = 'admin'
        return HttpResponseRedirect(reverse("App_Login:admin_dashboard"))
    elif teacher.exists():
        admin = 'teacher'
        teacher = teacher[0]
        if not teacher.is_fully_filled():
            messages.info(request, "Please fill up all the fields!")
            return HttpResponseRedirect(reverse('App_Teacher:update_profile', kwargs={'pk':teacher.user.pk}))
    else:
        return HttpResponseRedirect(reverse("App_Login:dashboard"))
    return render(request, 'App_Teacher/teacher_profile.html', context={'admin': admin, 'teacher': teacher})





