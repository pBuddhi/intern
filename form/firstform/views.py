from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import GuestForm
from .forms import EnquiryForm,RequirementForm,DatabaseForm
from .models import Guest,DatabaseInsert,Requirement

def index(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('enquiry')
    else:
        form = GuestForm()
        return render(request,'firstform/index.html',{'form':form})

def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.requirement = Guest.objects.latest('id')
            post.save()
            return redirect('index')
    else:
        form = EnquiryForm()
        return render(request,'firstform/enquiry.html',{'form':form})

def require(request):
    if request.method == 'POST':
        username = request.POST.get('username',False)
        phone = request.POST.get('phone',False)
        database_obj = DatabaseInsert(username=username,phone=phone)
        database_obj.save()
        guestlist = DatabaseInsert.objects.all()
        guestlist = guestlist[::-1]
        return render(request,'firstform/newrequire.html',{'guestlist':guestlist})
    else:
        guestlist = DatabaseInsert.objects.all()
        guestlist = guestlist[::-1]
        return render(request,'firstform/newrequire.html',{'guestlist':guestlist})


def database(request):
    if request.method == 'POST':
        mehman_username = request.POST.get('guestname','')
        mehman = DatabaseInsert.objects.get(username=mehman_username)
        query = request.POST.get('query','')
        requirement_obj = Requirement(mehman=mehman,query=query)
        requirement_obj.save()
        return redirect('requirement')
        
    
# Create your views here.
