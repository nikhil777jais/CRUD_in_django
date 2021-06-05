from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll.models import Student
from enroll.forms import StudentRegistration
# Create your views here.
def add_data(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            stu = Student(name=nm, email=em, password=ps)
            stu.save()
        fm = StudentRegistration()
    else:    
        fm = StudentRegistration()
    stud = Student.objects.all();
    return render(request, 'enroll/add.html', {'form':fm, 'stu':stud})

def delete_data(request, id ):
    pi =  Student.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/add/')

def update_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()   
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/update.html', {'form':fm,})
