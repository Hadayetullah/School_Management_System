from django.urls import path
from App_Payment import views

app_name = "App_Payment"


urlpatterns = [
    path('admission_fee/', views.pay_admission_fee, name='admission_fee'),
    path('status/', views.complete, name='complete'),
    path('pay/<val_id>/<tran_id>/', views.payment_completed, name='pay'),
]
