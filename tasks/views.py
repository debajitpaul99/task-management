from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskModelForm
from tasks.models import Employee, Task

# Create your views here.
def manager_dashboard(request):
    return render(request,'dashboard/manager_dashboard.html')

def user_dashboard(request):
    return render(request,'dashboard/user_dashboard.html')

def test(request):
    context = {
        "name": ['Debajit','Shri','Aury']
    }
    return render(request,'test.html',context)

def task_form(request):
    form = TaskModelForm() # This form is for GET method
    if request.method == "POST":
        form = TaskModelForm(request.POST) # This form is for POST method
        if form.is_valid():
            form.save()
            return render(request, "task_form.html", {"form2": form, "message": "Task added successfully"})
    context = {"form1": form}
    return render(request, "task_form.html",context)

def view_tasks(request):
    tasks = Task.objects.all()
    task2 = Task.objects.get(pk=2)
    return render(request, "task_view.html", {"all_tasks":tasks, "task2":task2})