from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from datetime import datetime
from django.db.models import Case, When
from django.shortcuts import get_object_or_404


def index(request):
    try:        
        db = Task.objects.all().order_by('due_date', Case(
            When(priority='High', then=0),
            When(priority='Medium', then=1),
            When(priority='Low', then=2),
            default=3
        ))
        context = {
            "db": db,
            "update": None
        }
        return render(request, "app/index.html", context)
    except Exception:
        return HttpResponse({'message':'Something went wrong, please contact the administrator'})


def insert(request):
    try:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            title = request.POST["title"]
            due_date = request.POST["due_date"]
            due_date2 = datetime.strptime(
                due_date, "%Y-%m-%d").date()
            description = request.POST["description"]
            priority = request.POST["priority"]
            if title == '' or due_date == '' or description == '' or priority == '':
                raise ValueError("there can be no empty text")
            db_data = Task(title=title, due_date=due_date2,
                        description=description, priority=priority)
            db_data.save()
            message = f'register succesful'
            response = JsonResponse({'message': message})
            response.status_code = 201
            return response
    except Exception:
        return HttpResponse({'message':'Something went wrong, please contact the administrator'})
    

def tasks_completed(request):
    try:
        db = Task.objects.filter(completed=True).order_by(
            'due_date',
            Case(
                When(priority='High', then=0),
                When(priority='Medium', then=1),
                When(priority='Low', then=2),
                default=3
            )
        )
        context = {
            "db": db,
            "update": None
        }
        return render(request, "app/index.html", context)
    except Exception:
        return HttpResponse({'message':'Something went wrong, please contact the administrator'})


def update_form(request, task_id):
    try:
        db = Task.objects.all().order_by('due_date', Case(
            When(priority='High', then=0),
            When(priority='Medium', then=1),
            When(priority='Low', then=2),
            default=3
        ))
        db_only = Task.objects.get(pk=task_id)
        context = {
            "db": db,
            "update": db_only
        }
        return render(request, "app/index.html", context)
    except Exception:
        return HttpResponse({'message':'Something went wrong, please contact the administrator'})
    


def update(request):
    try:
        id = request.POST["id"]
        title = request.POST["title"]
        description = request.POST["description"]
        due_date_str = request.POST["due_date"]      
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        priority = request.POST["priority"]
        db_data = Task.objects.get(pk=id)
        db_data.title = title
        db_data.description = description
        db_data.due_date = due_date
        db_data.priority = priority    
        db_data.save()
        return HttpResponseRedirect(reverse("index"))
    except Exception:
        return HttpResponse({'message':'Something went wrong, please contact the administrator'})


def update_completed(request, task_id):
    try:
        task = get_object_or_404(Task, pk=task_id)
        if task.completed:
            task.completed = False
        else:
            task.completed = True
        task.save()
        return HttpResponseRedirect(reverse("index"))
    except Exception:
            return HttpResponse({'message':'Something went wrong, please contact the administrator'})
        

def delete(request, task_id):
    try:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':            
            db_data = Task.objects.filter(id=task_id)
            db_data.delete()
            message = f'deleted succesful'
            response = JsonResponse({'message': message})
            response.status_code = 201
            return response                 
    except Exception:
        return HttpResponse({'message':'Something went wrong, please contact the administrator'})                
