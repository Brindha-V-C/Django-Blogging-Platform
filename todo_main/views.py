from django.shortcuts import render
from todo.models import Tasks

def home(request):
    tasks = Tasks.objects.filter(is_completed=False)
    context = {
        'tasks' : tasks,
    }
    return render(request, 'index.html', context)