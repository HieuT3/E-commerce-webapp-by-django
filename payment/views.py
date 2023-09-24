from django.shortcuts import render

from . models import ShippingAddress

def checkout(request):

    # Authenticated user

    if request.user.is_authenticated:

        try:

            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = {'shipping' : shipping_address}

            return render(request, 'payment/checkout.html', context)
        
        except ShippingAddress.DoesNotExist:

            return render(request, 'payment/checkout.html')

    else:

        return render(request, 'payment/checkout.html')
    

def complete_order(request):

    pass


def payment_success(request):

    return render(request, 'payment/payment-success.html')


def payment_failed(request):

    return render(request, 'payment/payment-failed.html')
