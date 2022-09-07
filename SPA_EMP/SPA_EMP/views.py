from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


def emp(request):
    return render(request,"emp.html")

def test2(request):
    return render(request,"test2.html")

def test3(request):
    return render(request,"test3.html")

def test4(request):
    return render(request,"test4.html")

def test5(request):
    return render(request,"test5.html")
def test6(request):
    return render(request,"test6.html")
