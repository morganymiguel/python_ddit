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

e_id = '6'            
sql1 = f"""DELETE FROM EMP
            WHERE E_ID = '{e_id}'"""
print(sql1)
cnt = cur.execute(sql1)

print("cnt",cnt)

sql = "SELECT * FROM EMP"
cur.execute(sql)
res = cur.fetchall()
for data in res:
    print(data)


cur.close()
con.close()

           

