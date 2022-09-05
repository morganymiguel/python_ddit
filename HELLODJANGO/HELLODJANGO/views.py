from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from HELLODJANGO.daoemp import DaoEmp
from django.shortcuts import render

def helloworld(request):
    return HttpResponse("Hello World")

@csrf_exempt
def myparam(request):
        # a = request.GET.get('a', '000')
        # return HttpResponse("param: "+a)
        a= request.POST['a']
        return HttpResponse("param: "+a)
        
def db(request):
    de = DaoEmp()
    list = de.mylist()
    txt =""
    for e in list:
        txt += "{},{},{},{}<br/>".format(e['e_id'],e['e_name'],e['sex'],e['addr'])
    
    return HttpResponse(txt)

def forward(request):
    a="홍길동"
    b=["전우치","신사임당","허균"]
    de= DaoEmp()
    mylist = de.mylist()
    # mylist = ['e_id':'1','e_name':'1','sex': '1','addr': '1',
              # 'e_id':'2','e_name':'2','sex': '2','addr': '2',
              # 'e_id':'3','e_name':'3','sex': '3','addr': '3']
    data = {
        'a': a,
        'b': b,
        'mylist': mylist
         }
    return render(request,"forward.html", data)

def emp(request):
    de = DaoEmp()
    mylist = de.mylist()
    data = {
        'mylist': mylist 
        }
    return render(request,"emp.html", data)