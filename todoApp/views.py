from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views.generic import ListView,UpdateView,CreateView,DetailView,DeleteView
from django.contrib.auth.decorators import login_required



def login_view(req):  # Renamed the function to login_view
    return render(req, 'login.html')

def register(req):
    if req.method == 'POST':
        form = Regform(req.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = Regform()
    return render(req, 'regform.html', {'form': form})

def loginuser(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            print('login success')
            return redirect(home1)
    else:
        print('authentication failed')
    return render(req, 'login.html')

def logoutuser(req):
    logout(req)
    return redirect(loginuser)


class TodoCreate(CreateView):
    model=Todo
    fields='__all__'
    template_name='addTodo.html'
    context_object_name='form'
    success_url='/todoApp/todolist'

class ProjectCreate(CreateView):
    model=Project
    fields='__all__'
    template_name='addProject.html'
    context_object_name='form'
    success_url='/todoApp/home1'


class Todolist(ListView):
    model=Todo
    template_name='listTodo.html'
    context_object_name='todo'

class Projectlist(ListView):
    model=Project
    template_name='listProject.html'
    context_object_name='todo'

class Projectlist2(ListView):
    model=Project
    template_name='viewProject.html'
    context_object_name='todo'

class TodoUp(UpdateView):
    model=Todo
    context_object_name='up'
    template_name='addTodo.html'
    fields='__all__'
    success_url='/todoApp/todolist'

class ProjectUpdate(UpdateView):
    model=Project
    context_object_name='up'
    template_name='addProject.html'
    fields='__all__'
    success_url='/todoApp/projectlist'

class TodoDelt(DeleteView):
    model=Todo
    success_url='/todoApp/todolist'
    template_name='deleteTodo.html'
    context_object_name='form'

class ProjectDelt(DeleteView):
    model=Project
    success_url='/todoApp/projectlist'
    template_name='deleteTodo.html'
    context_object_name='form'


def home(request):
    # Retrieve both completed and pending todos
    completed_todos = Todo.objects.filter(status='COMPLETE')
    pending_todos = Todo.objects.filter(status='PENDING')
    
    total_todos = Todo.objects.count()
    total_completed_todos = completed_todos.count()
    
    # Retrieve all projects with their todos
    projects = Project.objects.prefetch_related('todos')

    for project in projects:
        completed_count = project.todos.filter(status='COMPLETE').count()
        setattr(project, 'completed_count', completed_count)

    return render(request, 'home.html', {
        'completed_todos': completed_todos,
        'pending_todos': pending_todos,
        'total_todos': total_todos,
        'total_completed_todos': total_completed_todos,
        'projects': projects,
    })
@login_required
def home1(req):
    return render(req,'home1.html')

def project_details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    pending_todos = project.todos.filter(status='PENDING')
    completed_todos = project.todos.filter(status='COMPLETE')
    total_todos = project.todos.count()
    total_completed_todos = completed_todos.count()
    return render(request, 'projectDetails.html', {
        'project': project,
        'pending_todos': pending_todos,
        'completed_todos': completed_todos,
        'total_todos': total_todos,
        'total_completed_todos': total_completed_todos,
    })