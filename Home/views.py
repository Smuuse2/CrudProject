from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from django.contrib import messages
from .forms import studentForm
# Create your views here.
def Home(request):
    form = studentForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, 'add.html', {'form': form})


def base(req):
    return render(req, 'base.html')

def show(req):
    alldata = Student.objects.all()
    context = {
        's': alldata
    }
    return render(req, 'show.html', context)

def update(req, id):
    student = Student.objects.get(id=id)
    form = studentForm(req.POST, instance=student) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(req, 'update.html',{'student': student})

def delete(req,id):
    form = Student.objects.get(id=id)
    messages.success(req, "Deleted")
    form.delete()

    return HttpResponseRedirect('/')