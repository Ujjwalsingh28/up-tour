from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from django.db import connections
from .models import *


# Create your views here.

def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def destinations(request):
    return render(request,'destinations.html')

def gallery(request):
    data=tbl_gallery.objects.all()
    md={"pdata":data}
    return render(request,'gallery.html',md)

def contactus(request):
    mydict={}

    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('address')
        d=request.POST.get('subject')
        e=request.POST.get('msg')
        contact(Name=a, Email=b, Address=c, Subject=d, Message=e).save()
        return HttpResponse("<script>alert('Data save successful');location.href='/contactus'</script>")


    return render(request,'contactus.html', mydict)
def faqs(request):
    return render(request,'faqs.html')
def varanasi(request):
    return render(request,'varanasi.html')
def vrindavan(request):
    return render(request,'vrindavan.html')
def agra(request):
    return render(request,'agra.html')
def lucknow(request):
    return render(request,'lucknow.html')
def prayagraj(request):
    return render(request,'prayagraj.html')
def chitrakoot(request):
    return render(request,'chitrakoot.html')
def ayodhya(request):
    return render(request,'ayodhya.html')
def raebareli(request):
    return render(request,'raebareli.html')
def mirzapur(request):
    return render(request,'mirzapur.html')
def pratapgarh(request):
    return render(request,'pratapgarh.html')
def etawah(request):
    return render(request,'etawah.html')
def kanpur(request):
    return render(request,'kanpur.html')
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        x = tbl_register.objects.all().filter(email=email).count()
        if x == 1:
            return HttpResponse("<script>alert('You are already registered..');""location.href='/register'</script>")
        else:
            tbl_register(name=name, email=email, password=passwd, address=address, mobile=mobile, pincode=pincode,
                         city=city, ).save()
            return HttpResponse("<script>alert('Thanks for register with us...');location.href='/register'</script>")

    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get('userid')
        passwd=request.POST.get('passwd')
        x=tbl_register.objects.all().filter(email=email,password=passwd).count()

        if x==1:
            y=tbl_register.objects.all().filter(email=email)
            request.session['name']=str(y[0].name)
            request.session['user'] = email

            return HttpResponse("<script>alert('you are login successfully..');location.href='/destinations';</script>")
        else:
            return HttpResponse("<script>alert('your userid or password is incorrect..');location.href='/login';</script>")


    return render(request,'login.html')

def logout(request):
    if request.session.get('user'):
        del request.session['user']
        return HttpResponse("<script>alert('Now you are logout..');location.href='/login';</script>")
    return render(request,'logout.html')