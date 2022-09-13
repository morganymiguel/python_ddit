from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from SPA_EMP.daoemp import DaoEmp

de = DaoEmp();

def emp(request):
    return render(request,"emp.html")
def emp_list_ajax(request):
    list = de.mylist()
    context = {
        "list": list
    }
    return JsonResponse(context)
def emp_detail_ajax(request):
    e_id = request.GET.get('e_id','000')
    emp= de.myone(e_id)
    context = {
        'emp': emp
    }
    return JsonResponse(context)

@csrf_exempt
def emp_insert_ajax(request):
    e_id = request.POST["e_id"]
    e_name = request.POST["e_name"]
    sex = request.POST["sex"]
    addr = request.POST["addr"]
    
    cnt = de.myinsert(e_id, e_name, sex, addr)
    
    context = {
        'cnt': cnt
    }
    return JsonResponse(context)
@csrf_exempt
def emp_update_ajax(request):
    e_id = request.POST["e_id"]
    e_name = request.POST["e_name"]
    sex = request.POST["sex"]
    addr = request.POST["addr"]
    
    cnt = de.myupdate(e_id, e_name, sex, addr)
    
    context = {
        'cnt': cnt
    }
    return JsonResponse(context)
    
@csrf_exempt
def emp_delete_ajax(request):
    e_id = request.POST["e_id"]
    
    cnt = de.mydelete(e_id)
    
    context = {
        'cnt': cnt
    }
    return JsonResponse(context)
    

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
def jqtest1(request):
    return render(request,"jqtest1.html")
def jqtest2(request):
    return render(request,"jqtest2.html")
def jqtest3(request):
    return render(request,"jqtest3.html")
def jqtest4(request):
    return render(request,"jqtest4.html")
def jqtest5(request):
    return render(request,"jqtest5.html")
def jqtest6(request):
    return render(request,"jqtest6.html")

