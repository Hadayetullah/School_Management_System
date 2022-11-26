from django.contrib import admin
from App_Attendance.models import Attendance


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["user", "student", "class_no", "present", "created", "session"]

    class Meta:
        model = Attendance



admin.site.register(Attendance, AttendanceAdmin)
