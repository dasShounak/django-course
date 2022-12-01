from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
# def index(request):
#     return HttpResponse("<em>My Second Project</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)

def index(request):
    return render(request,'appTwo/index.html')

def form(request):
    form = forms.UserRegisterForm()

    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('ERROR: Form Invalid')

    return render(request,'appTwo/users.html',context={'form':form})
