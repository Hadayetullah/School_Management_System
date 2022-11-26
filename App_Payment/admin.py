from django.contrib import admin
from App_Payment.models import Payments

# Register your models here.
class PaymentView(admin.ModelAdmin):
    list_display = ["user", "created", "paymentId", "orderId"]
    
    class Meta:
        model = Payments

admin.site.register(Payments, PaymentView)
