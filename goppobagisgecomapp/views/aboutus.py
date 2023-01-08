from django.shortcuts import render , redirect , HttpResponseRedirect

def aboutus(request):
    data={}
    return render(request, "about-us.html",data)