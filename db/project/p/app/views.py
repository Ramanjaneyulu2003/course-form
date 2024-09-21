from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Student
# Create your views here.
def index(request):
    return HttpResponse("hey")
def courseform(request):
    return render(request,'course_form.html')
def display(request):
    if request.method=='POST':
        x=request.POST['sname']
        y=request.POST['scourse']
        z=request.POST['sfees']
        c=Student.objects.create(sname=x,scourse=y,sfees=z)
        c.save()
    return redirect("/")
def dashboard(request):
    content={}
    content['data']=Student.objects.all()
    return render(request,'dashboard.html',content)
def delete(request,rid):
    x=Student.objects.get(id=rid)
    x.delete()
    return redirect('/')