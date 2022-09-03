from django.http.response import HttpResponse
from aiohttp.client import request
from conda_build import render
from django.views.decorators.csrf import csrf_exempt
import pymysql

def helloworld(request):
    return HttpResponse("Hello World")

@csrf_exempt
def myparam(request):
        # a = request.GET.get('a', '000')
        # return HttpResponse("param: "+a)
        a= request.POST['a']
        return HttpResponse("param: "+a)
        
def db(request):
    


    con = pymysql.connect(host= '127.0.0.1',user = 'root', password = 'python',
    db = 'python', charset='utf8',port =3305,
    autocommit = True,
    cursorclass=pymysql.cursors.DictCursor
    )
    cur = con.cursor()

    sql = "SELECT * FROM EMP"

    cur.execute(sql)
    res = cur.fetchall()
    a =""
    for data in res:
        a =a + data +"\n"
    return HttpResponse("db\n"+ a)