from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import * 

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        cname=request.POST.get(cname)
        email=request.POST.get(email)
        pno=request.POST.get(pno)
        un=request.POST.get(un)
        pw=request.POST.get(pw)
        customer=Customer(cname=cname, email=email, pno=pno, un=un, pw=pw)
        customer.save()
        return HttpResponse('Registered successfully')
    return render(request,'register.html')
def register_django_forms(request):
    ECFO=CustomerForm()
    d={'ECFO':ECFO}
    if request.method=='POST':
        name=request.POST.get(name)
        email=request.POST.get(email)
        pno=request.POST.get(pno)
        un=request.POST.get(un)
        pw=request.POST.get(pw)
        customer=CustomerForm(name=name, email=email, pno=pno, un=un, pw=pw)
        customer.save()
        return HttpResponse('Registered')

    return render(request,'register_django_forms.html',d)
