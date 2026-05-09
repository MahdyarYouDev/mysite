from django.shortcuts import render 
from django.http import HttpResponse

def index_view(request):
    return render(request,'in1.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')

