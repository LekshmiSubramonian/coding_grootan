from django.http.response import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def display(request):
    response=requests.get('https://userslists.free.beeceptor.com/userslists').json()
    #print(response)
    result=response['data'][0]
    #print(result)
    return render(request,'display.html',{'result':result})

def more(request):
    query=int(request.GET['seemore'])
    response=requests.get('https://userslists.free.beeceptor.com/userslists').json()
    result=response['data'][query-1]
    print(result)
    return render(request,"more.html",{'more':result})


def next(request):
    query=int(request.GET['next'])
    response=requests.get('https://userslists.free.beeceptor.com/userslists').json()
    l=len(response)
    #print("length:",l)
    if query>l:
        return HttpResponse("end user")
    else:
        result=response['data'][query]
    return render(request,"next.html",{'next':result})


def previous(request):
    query=int(request.GET['previous'])
    if query <= 1:
        return HttpResponse("end user")
    else:
        response=requests.get('https://userslists.free.beeceptor.com/userslists').json()
        result=response['data'][query-2]
    return render(request,"previous.html",{'previous':result})