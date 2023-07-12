from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.

def register(request):
    if request.method == 'POST':
        errors = User.objects.Validate_Registration(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # Hash the password
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        # Create a user
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_pw,
            role=request.POST['role'],
            secret_password=request.POST['secret_password']

        )
        # Create a session
        request.session['user_id'] = new_user.id
        return redirect('/all_tasks')
    return redirect('/all_tasks')



def login(request):
    if request.method == 'POST':
        log_email = request.POST['log_email']
        log_password = request.POST['log_password']
        log_role = request.POST['log_role']

        try:
            user = User.objects.get(email=log_email, role=log_role)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return redirect('/')

        if bcrypt.checkpw(log_password.encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/all_tasks')

        messages.error(request, 'Invalid email or password')
        return redirect('/')

    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):
    return render(request, 'index.html')

def create_task(request):
    context = {
        'this_user':User.objects.get(id = request.session['user_id']),
        'users': User.objects.all(),
        
    }
    return render(request, 'create_task.html', context)

def user_remove(request):
    context = {
        'this_user':User.objects.get(id = request.session['user_id']),
        'users': User.objects.all(),
        
    }
    return render(request, 'remove_user.html', context)


# def remove_user(request, user_id):
#     if request.method == 'POST':
#         try:
#             user = User.objects.get(id=user_id)
#             user.delete()
#             return redirect('/all_tasks')
#         except User.DoesNotExist:
#             # Handle the case when the user is not found
#             # You can show an error message or redirect to an appropriate page
#             pass
#     return redirect('/')

def remove_user(request):
    if request.method == 'POST':
        try:
            assigned_to_id = request.POST.get('assigned_to')
            user = User.objects.get(id=assigned_to_id)
            # user = User.objects.get(id=user_id)
            if user.role in ['manager', 'employee']:
                user.delete()
            return redirect('/all_tasks')
        except User.DoesNotExist:
            # Handle the case when the user is not found
            # You can show an error message or redirect to an appropriate page
            pass
    return redirect('/')




def task_creation(request):
    if request.method == 'POST':
        assigned_to_id = request.POST.get('assigned_to')
        assigned_to_user = User.objects.get(id=assigned_to_id)
        creator = User.objects.get(id=request.session['user_id'])

        if creator.role == 'executive' and assigned_to_user.role == 'manager':
            # CEO can assign tasks to managers only
            task = Task.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                due_date=request.POST['due_date'],
                creator=creator
            )
            task.assigned_user.add(assigned_to_user)

        elif creator.role == 'manager' and assigned_to_user.role == 'employee':
            # Manager can assign tasks to employees only
            task = Task.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                due_date=request.POST['due_date'],
                creator=creator
            )
            task.assigned_user.add(assigned_to_user)

        elif creator.role == 'head' and assigned_to_user.role in ['manager', 'employee']:
            # Head can assign tasks to managers and employees
            task = Task.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                due_date=request.POST['due_date'],
                creator=creator
            )
            task.assigned_user.add(assigned_to_user)

        else:
            # Handle the case when the assignment is not allowed
            # You can show an error message or redirect back to the task creation page
            # with an appropriate message.
            # For simplicity, I'm redirecting back to the task creation page here.
            return redirect('/create_task')

    return redirect('/all_tasks')


def delete_task(request, id):
        destroyed = Task.objects.get(id=id)
        destroyed.delete()
        return redirect('/all_tasks')



def edit(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    task = Task.objects.get(id=id)
    context = {
        'this_user':User.objects.get(id = request.session['user_id']),
        'task':task,
        'user':this_user[0],
        'users': User.objects.all(),
        'tasks':Task.objects.all()
    }
    return render(request,'edit_task.html', context)

def update_task(request, id):
    if request.method == 'POST':
        errors = Task.objects.Task_Validator(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/edit_task')
    edit_task = Task.objects.get(id=id)

    edit_task.due_date = request.POST['update_due_date']
    edit_task.title = request.POST['Update_Title']
    edit_task.description = request.POST['update_description']
    edit_task.save()
    return redirect('/all_tasks')

def all_tasks(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        context = {
            'this_user': user,
            'tasks': Task.objects.all(),
            'users': User.objects.all(),
            'role': user.role
        }
        return render(request, 'all_tasks.html', context)
    else:
        return redirect('/')



def view_task(request, id):
    context = {
        'task':Task.objects.get(id = id)
        
}
    return render(request, 'view_task.html', context)

def complete_task(request, id):
    context = {
        'task':Task.objects.get(id = id)
    }
    return render(request,'complete_task.html', context)

def task_completion(request, id):
    if request.method == 'POST':
        complete_notes = Complete.objects.create(completion_notes = request.POST['completion_notes'], date_completed = request.POST['completion_date'],status = int(request.POST['status']), task = Task.objects.get(id = id))
    return redirect('/all_tasks')