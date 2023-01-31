from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect

class ContactUs(View):
    def get(self,request):
        return render(request, 'contactus.html')

    def post(self,request):
        return render(request, 'contactus.html')
