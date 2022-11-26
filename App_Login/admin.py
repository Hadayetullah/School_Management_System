from django.contrib import admin
from App_Login.models import User, Profile

# Register your models here.
admin.site.register(User)

class ProfileView(admin.ModelAdmin):
    list_display = ["user", "full_name", "dob", "gender", "select_class"]
    
    class Meta:
        model = Profile

admin.site.register(Profile, ProfileView) 
