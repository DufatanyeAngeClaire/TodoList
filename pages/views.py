from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import Task
from django.utils import timezone

# Create your views here.
# Implement the following functionalities through Django views and corresponding HTML templates:
# 1- View To-Do Lists: 
# A page that displays all tasks in the to-do list.
# 2- Add New Task: 
# A form to allow users to add a new task to the list.
# 3- Update Task Status:
# Functionality to change the status of a task (e.g., mark as completed or pending). This could be a link/button next to each task.
# 4- Delete Task: 
# Functionality to remove a task from the list. This could be a link/button next to each task


def view_task(request):
    all_task = Task.objects.all
    return render(request,' view.html', {'all':all_task})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status", "Pending")
        date = request.POST.get("date")

        if not date:
            date = timezone.now()



        if title and description and status :  # avoid inserting empty values
            Task.objects.create(
                title=title,
                description=description,
                date=date
            )
        return redirect('/task/')

    # For GET requests — render the form page
    return render(request, "add_task.html")
