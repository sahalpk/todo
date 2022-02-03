
from django.db.models.base import Model
from django.shortcuts import redirect, render
from .forms import Todoform
from .models import Task
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class TaskListview(ListView):
    model=Task
    template_name= 'home.html'
    context__object_name ='task'

class TaskDetailview(DetailView):
    model=Task
    template_name='details.html'
    context__object_name ='task'

class TaskUpdateview(UpdateView):
    model=Task
    template_name='update.html'
    context__object_name ='task'
    fields=('name','priority','date')

    def  get_success_url(self) :
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class TaskDeleteview(DeleteView):
    model=Task
    template_name='delete.html'
    success_url= reverse_lazy('cbvhome')

# Create your views here.

def add(request):
    task=Task.objects.all()
    
    if request.method == "POST":
        name=request.POST.get("name","")
        priority=request.POST.get("priority","")
        date=request.POST.get("date","")
        task=Task(name=name,priority=priority,date=date)
        task.save() 
        return redirect('/')      
    
    return render(request,"home.html",{'task':task}) 

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or None , instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'f':f,'task':task})

