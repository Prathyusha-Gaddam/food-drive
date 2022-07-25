from django.shortcuts import render,redirect
from .models import fooddetails
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for { username }! You are able to login now')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'food/register.html',{'form':form})

@login_required
def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        iname=request.POST.get('iname')
        itype=request.POST.get('itype')
        location=request.POST.get('location')
        hlevel=request.POST.get('hlevel')
        email=request.POST.get('email')
        time=request.POST.get('time')
        date=request.POST.get('date')
        mobileno=request.POST.get('mobileno')
        en=fooddetails(Nameofdonor=name,Itemname=iname,Itype=itype,Hlevel=hlevel,Location=location)
        en.save()
    return render(request,'food/index.html')

def getdetails(request):
    details=fooddetails.objects.all()
    return render(request,'food/details.html',{'details':details})

def home(request):
    return render(request,'food/Home1.html')


def about(request):
    return render(request,'food/about.html')

def contact(request):
    return render(request,'food/contact.html')

def logout(request):
    return render(request,'food/logout.html')