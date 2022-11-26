from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse

from App_Login.models import Profile
from App_Payment.models import Payments


from django.contrib.auth.decorators import login_required

# For Payment
# import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt


from django.contrib import messages


# Create your views here.
@login_required
def pay_admission_fee(request):
    profile = Profile.objects.get(user=request.user, admitted=False)
    if not profile.is_fully_filled():
        messages.info(request, "Please complete your profile details!")
        return HttpResponseRedirect(reverse("App_Login:change_profile"))

    # SSLCommerz Code
    store_id = 'abc62b7f4a85d03a'
    API_key = 'abc62b7f4a85d03a@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)

    status_url = request.build_absolute_uri(reverse("App_Payment:complete"))
    # print(status_url)

    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url,
    ipn_url=status_url)

    fee = Profile.objects.get(user=request.user, admitted=False)
    total_fee = fee.admission_fee()

    mypayment.set_product_integration(total_amount=Decimal(total_fee), currency='BDT',
    product_category='Fee', product_name="Fess", num_of_item=1,
    shipping_method='Courier', product_profile='None')

    current_user = request.user

    mypayment.set_customer_info(name=current_user.profile.full_name, email=current_user.email,
    address1=current_user.profile.present_address, address2=current_user.profile.present_address, city=current_user.profile.sub_district,
    postcode=current_user.profile.zipcode, country=current_user.profile.country, phone=current_user.profile.phone)

    mypayment.set_shipping_info(shipping_to=current_user.profile.full_name, address=current_user.profile.present_address,
    city=current_user.profile.sub_district, postcode=current_user.profile.zipcode, country=current_user.profile.country)

    response_data = mypayment.init_payment()
    # print(response_data)
    # return render(request, "App_Payment/payment.html", context={})
    return redirect(response_data['GatewayPageURL'])


@csrf_exempt
def complete(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        # print(payment_data)
        # print(payment_data['status'])
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request, f"Your Payment Completed Successfully!")
            return HttpResponseRedirect(reverse("App_Payment:pay", kwargs={'val_id': val_id, 'tran_id': tran_id}))
        elif status == 'FAILED':
            messages.warning(request, f"Your Payment Failed! Please Try Again! Page will be redirected")

    return render(request, "App_Payment/complete.html", context={})


@login_required
def payment_completed(request, val_id, tran_id):
    payment = Payments.objects.get_or_create(user=request.user)[0]
    payment.due = False
    payment.orderId = tran_id
    payment.paymentId = val_id
    payment.save()

    profile = Profile.objects.get(user=request.user, admitted=False)
    profile.admitted = True
    profile.save()
    return HttpResponseRedirect(reverse("App_Login:dashboard"))
