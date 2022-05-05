from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from postal.models import Userreg


def home(request):
    return render(request, 'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def services(request):
    return render(request,'services.html')
def Aboutus(request):
    return render(request,'Aboutus.html')

def home1(request):
    return render(request,'home1.html')


def booking(request):
    return render(request,'booking.html')

def sample(request):
    if not 'uname' in request.session:
        return redirect('loginpage')
    uname = request.session['uname']
 
    return render(request, 'sample.html', {'uname': uname})


def Userregestration(request):
    if 'uname' in request.session:
        return redirect('travel')
    if request.method=="POST":
       
        uname = request.POST.get('uname')
      
        umailObj = Userreg.objects.all().filter(uname=uname)
        if not umailObj:
            saverecord=Userreg() 
            saverecord.name=request.POST.get('name')
            saverecord.address=request.POST.get('address')
            saverecord.uname=request.POST.get('uname')
            saverecord.pwd=request.POST.get('pwd')
            saverecord.save()
            messages.success(request,"  Regestration is succesfull!.....")
            print("  Regestration is succesfull!.....")
            request.session['uname']=uname
            return redirect('sample')
        else:
            print("User Already Exists")
            return redirect('login')
    return render(request,'signup.html')