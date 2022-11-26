from django.contrib import admin
from .models import Grade

# Register your models here.
class GradeView(admin.ModelAdmin):
    list_display = ["user", "full_name", "class_no", "subject", "roll", "test1", "test2", "test3", "test4", "test5", "midterm", "test6", "test7", "test8", "test9", "test10", "final"]
    
    class Meta:
        model = Grade

admin.site.register(Grade, GradeView)
