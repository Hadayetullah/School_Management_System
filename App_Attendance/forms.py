from django import forms
from App_Attendance.models import Attendance


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('present', 'absent',)
