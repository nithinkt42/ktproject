from django.shortcuts import render
from django.http import HttpResponse


def nithin(request):
    return HttpResponse("hello nithin")

def htmlpage(request):
    return render(request,'appkt templates/appkthtml.html')   
     
