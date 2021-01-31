from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
# Create your views here


def about(request):
    return render(request,'about.html')

def index(request):
    if request.method=='GET':
        return redirect('/')
  
     









    
        
