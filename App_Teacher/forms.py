from django import forms

from App_Login.models import User
from App_Teacher.models import Teacher


# Teacher Profile Creation Form
class TeacherForm(forms.ModelForm):
    select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(choices=select_gender, widget=forms.RadioSelect())
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    # subject_2 = forms.ChoiceField(initial='Bangla 1st paper')
    class Meta:
        model = Teacher
        exclude = ('user', 'id_no', 'teacher', 'admin',)


# class AddNewTeacher(forms.ModelForm):
#     select_gender = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     )
#     gender = forms.ChoiceField(choices=select_gender, widget=forms.RadioSelect())
#     dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
#     class Meta:
#         model = Teacher
#         exclude = ('user',)
