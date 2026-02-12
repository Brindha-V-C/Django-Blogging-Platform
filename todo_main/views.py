from django.shortcuts import render
from todo.models import Tasks

def home(request):
    tasks = Tasks.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Tasks.objects.filter(is_completed=True)
    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks,
    }
    return render(request, 'index.html', context)