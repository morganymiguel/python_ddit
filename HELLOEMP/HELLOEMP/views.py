from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from HELLOEMP.daoemp import DaoEmp 
from django.http import request
from django.utils.decorators import method_decorator

de = DaoEmp()



def emp(request):
    dblist = de.mylist()
    attr = {
        'dblist' : dblist
    }
    return render(request,'emp_list.html',attr)

def emp_add(request):
    return render(request, 'emp_add.html')

def emp_add_act(request):
    
    e_id = request.POST["e_id"]
    e_name = request.POST["e_name"]
    sex = request.POST["sex"]
    addr = request.POST["addr"]
    cnt = de.myinsert(e_id, e_name, sex, addr)
    
    attr = {
        'cnt': cnt
    }
    return render(request, "emp_add_act.html", attr)
        
def emp_detail(request):
    e_id = request.GET.get('e_id','__')
    emp = de.myone(e_id)
    
    attr = {
        
        'emp': emp
    }
    
    return render(request,"emp_detail.html",attr)
    