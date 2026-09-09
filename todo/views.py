from django.shortcuts import render , redirect , get_object_or_404
from todo.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todo.forms import Taskform

# Create your views here.

def home_view(request):
    return render(request,'todo/home.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request,'todo/task_list.html',{'context':tasks})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = UserCreationForm()
    return render(request,'todo/signup.html',{'form':form})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task')
    else:
        form = Taskform()
    return render(request, 'todo/add_task.html' , {'form':form})

@login_required
def edit_task(request , task_id):
    task = get_object_or_404(Task , id=task_id , user = request.user)

    if request.method == 'POST':
        form = Taskform(request.POST , instance=task)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task')
    else:
        form = Taskform(instance=task)

    return render(request , 'todo/edit_task.html' , {'form':form})