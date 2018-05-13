from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import ToDoData

# Create your views here.
#function based views



def index(request):
    return render(request, 'index.html')

def edittodo(request):
    return render(request, 'edittodo.html')

def edit(request, id):
    obj = ToDoData.objects.filter(pk=id)
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            obj.description = form.cleaned_data['description']
            obj.deadline = form.cleaned_data['deadline']
            obj.percent = form.cleaned_data['percent']
            
            args ={'list': ToDoData.objects.all()}
            return render(request,'ubersicht.html', args)
            
    else:
        form = ToDoForm()
        return render(request, 'edit.html',{'obj':obj,'form':form})

def delete(request, id):
    ToDoData.objects.filter(pk=id).delete()
    #args ={'list': ToDoData.objects.all()}
    return redirect('/TheToDos/ubersicht.html')


def newtodo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
          #process new data
          obj = ToDoData()
          obj.description = form.cleaned_data['description']
          obj.deadline = form.cleaned_data['deadline']
          obj.percent = form.cleaned_data['percent']
          #finally save ne object in db
          obj.save() 
          args ={'list': ToDoData.objects.all()}
          return render(request,'ubersicht.html', args)
    else:
        form= ToDoData()
        
        return render(request, 'newtodo.html',{'form': form})

def impressum(request):
    return render(request, 'impressum.html')

def ubersicht(request):
    #how you refert to the data in the template itself = 'name'
    # name of the variable here = :name
    args = {'list': ToDoData.objects.all()}
    return render(request, 'ubersicht.html', args)

