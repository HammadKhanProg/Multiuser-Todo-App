from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from app.models import TODO
from app.forms import TodoForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="signin")
def home (request):
    if request.user.is_authenticated:
        user=request.user
        tasks=TODO.objects.filter(user=user).order_by("priority")
        form=TodoForm()
        data={
            "form":form,
            "tasks":tasks
        }
        return render(request,"home.html",data)
    
def signup (request):
    if request.method=="GET":
        form=UserCreationForm()
        context={
            "form":form
        }
        return render (request,"signup.html",context)
    else:
        form=UserCreationForm(request.POST)
        context={
            "form":form
        }
        if form.is_valid():
            user=form.save()
            if user is not None:
                return redirect ("home")
        else:
            return render (request,"signup.html",context)


def signin (request):
    if request.method=="GET":
        form=AuthenticationForm()
        context={
            "form":form
        }
        return render(request,"signin.html",context)
    else:
        form=AuthenticationForm(data=request.POST)
        context={
            "form":form
        }
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user:
                login(request, user)
                return redirect ("home")
        else:
            return render(request,"signin.html",context)

def signout (request):
    logout(request)
    return redirect("signin")

@login_required(login_url="signin")
def add_todo (request):
    if request.user.is_authenticated:
        user=request.user
        print(user)
        form=TodoForm(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.user=user
            todo.save()
            print(form.cleaned_data)
            return redirect ("home")
        else:
            data={
        "form":form
        }
        return render(request,"home.html",data)
    
@login_required(login_url="signin")
def delete_todo(request,pk):
    task=TODO.objects.get(id=pk)
    task.delete()
    return redirect("home")

@login_required(login_url="signin")
def update (request,pk):
    task=TODO.objects.get(id=pk)
    form=TodoForm(instance=task)
    if request.method=="POST":
        form=TodoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect ("home")
    data={
        "form":form
    }
    return render (request,"update.html",data)
