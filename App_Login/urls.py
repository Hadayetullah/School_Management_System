from django.urls import path
from App_Login import views

app_name = "App_Login"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('student/', views.student_login, name='student_login'),
    path('admin_panel/', views.admin_login, name='admin_login'),
    path('teacher_panel/', views.teacher_login, name='teacher_login'),
    path('login/<user>/<value>/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('change_profile/', views.change_profile, name='change_profile'),
    path('admission_fee/', views.admission_fee, name='admission_fee'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('routine/', views.routine, name='routine'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teachers/', views.all_teacher, name='all_teacher'),
    path('teacher_info/<pk>/', views.teacher_info, name='teacher_info'),
    path('student_api/', views.StudentDetailAPIView.as_view()),
]
