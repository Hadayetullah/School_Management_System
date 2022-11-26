from django import forms
from App_Login.models import User, Profile

from django.contrib.auth.forms import UserCreationForm


# Forms
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class ProfileForm(forms.ModelForm):
    select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(choices=select_gender, widget=forms.RadioSelect())
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    
    class Meta:
        model = Profile
        exclude = ('user', 'admitted', 'roll', 'new_student', 'old_student', 'session')
