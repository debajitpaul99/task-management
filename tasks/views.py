from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskModelForm
from tasks.models import Employee, Task, TaskDetails, Project
from django.db.models import Q, Count, Max, Min, Avg

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
    # tasks = Task.objects.select_related("taskdetails").all()
    # task = Task.objects.prefetch_related("assigned_to").all()
    # task_count = Task.objects.aggregate(num_task=Count("id"))
    task_count = Project.objects.annotate(num_of_task=Count("task")).order_by("num_of_task")
    return render(request, "task_view.html", {"tasks": task_count})