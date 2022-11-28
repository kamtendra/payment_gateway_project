from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000
        order_currency = 'INR'
        order_receipt = 'order_receipt_11'
        client = razorpay.Client(auth=("rzp_test_9nmrK825fjo0Ym", "1f1icPZDRCKvac3lzpOmLSl1"))
        payment = client.order.create(amount=amount,currency=order_currency,receipt=order_receipt)
    return render(request, 'index.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")
