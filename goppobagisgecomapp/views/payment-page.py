from django.shortcuts import render, redirect, HttpResponseRedirect

def paymentSuccessful(request):
    return render(request, 'payment-success.html')

def paymentFaild(request):
    return render(request, 'payment-faild.html')