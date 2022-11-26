from django.urls import path
from App_Teacher import views

app_name = "App_Teacher"


urlpatterns = [
    path('update_profile/<pk>/', views.change_teacher_prof, name='update_profile'),
    path('profile/', views.teacher_profile, name="teacher_profile"),
]
