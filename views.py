from django.shortcuts import render, redirect
from .models import studentreg
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def registers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('mail')
        number = request.POST.get('number')
        age = request.POST.get('age')
        enrollmentdate = request.POST.get('enrollmentdate')
        course = request.POST.get('course')


        new_entry = studentreg(
            name=name,
            email=email,
            number=number,
            age=age,
            enrollmentdate=enrollmentdate,
            course=course
        )
        new_entry.save()
        return redirect('index')  
    return render(request, 'register.html')


def viewstudent(request):
    u=studentreg.objects.all()
    return render(request,'studentview.html',{'res':u})
