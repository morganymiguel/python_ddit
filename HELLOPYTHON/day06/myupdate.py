import pymysql


con = pymysql.connect(host= '127.0.0.1',user = 'root', password = 'python',
                           db = 'python', charset='utf8',port =3305,
                          autocommit = True,
                          cursorclass=pymysql.cursors.DictCursor
                          )
cur = con.cursor()

sql = "SELECT * FROM EMP"

cur.execute(sql)
res = cur.fetchall()
for data in res:
    print(data)

            
e_name = '9'
sex = '9'
addr= '9'
e_id ='3'
sql1 = f"""UPDATE EMP
             SET E_NAME ='{e_name}', SEX ='{sex}', ADDR ='{addr}'
           WHERE E_ID ='{e_id}' """
print(sql1)
cur.execute(sql1)

sql = "SELECT * FROM EMP"
cur.execute(sql)
res = cur.fetchall()
for data in res:
    print(data)


cur.close()
con.close()

           

