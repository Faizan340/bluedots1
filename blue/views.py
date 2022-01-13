from django.shortcuts import render, redirect
from .models import Form

from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request,'home.html')

def about1(request):
    return render(request,'about1.html')

def training(request):
    return render(request,'training.html')

def form1(request): 
    todo = Form.objects.all()
    if request.method == 'POST':
        new_todo = Form(
            fullname = request.POST['fullname'],
            email = request.POST['email'],
            number = request.POST['number'],
            address = request.POST['address'],
            xpercentage = request.POST['xpercentage'],
            xiipercentage = request.POST['xiipercentage'],
            training = request.POST['training'],
            city = request.POST['city']
        )
        new_todo.save()
        return render(request, 'success.html')
    return render(request,'form1.html')

def jobs(request):
    return render(request,'jobs.html')

def success(request):
    return render(request,'success.html')