from django.contrib import admin
from App_Teacher.models import Teacher

# Register your models here.
class TeacherView(admin.ModelAdmin):
    list_display = ["user", "full_name", "id_no", "dob", "gender", "subject_1", "subject_2",]
    
    class Meta:
        model = Teacher

admin.site.register(Teacher, TeacherView)
