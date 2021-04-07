from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo_user
# Create your views here.


def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['pass']
        res = auth.authenticate(username=user, password=password)
        if res is not None:
            auth.login(request, res)
            return redirect('todo')
        else:
            messages.info(request,'username/password is invalid')
            return redirect('login')

    return render(request, 'login.html')


@login_required(login_url='login')
def todo(request):
    if request.method == 'POST':
        taskname = request.POST['taskname']
        status = request.POST['status']
        desc = request.POST['desc']
        res = Todo_user(task=taskname, status=status,
                        desc=desc, user=request.user)
        res.save()
        return redirect('home')

    return render(request, 'todo.html')


@login_required(login_url='login')
def home(request):
    res = Todo_user.objects.filter(user_id=request.user)
    return render(request, 'home.html', {'res': res})


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email Already exists')
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username Already exists')
            return redirect('/register')    
        else:    
           res = User.objects.create_user(
            first_name=fname, last_name=lname, email=email, password=password, username=username)
           res.save()
        return redirect('/login')

    return render(request, 'register.html')


@login_required(login_url='login')
def update(request, id):
    res = Todo_user.objects.get(id=id)
    return render(request, 'update.html', {'res': res})


@login_required(login_url='login')
def dataupdate(request, id):
    res = Todo_user.objects.get(id=id)
    res.task = request.POST['taskname']
    res.status = request.POST['status']
    res.desc = request.POST['desc']
    res.save()
    return redirect('home')


@login_required(login_url='login')
def delete(request, id):
    res = Todo_user.objects.get(id=id)
    res.delete()
    return redirect('home')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
