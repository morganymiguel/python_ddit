# STEP 1
import pymysql


# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python', charset='utf8',port =3305,
                        autocommit=True, # 결과 DB 반영 (Insert or update)
                      cursorclass=pymysql.cursors.DictCursor # DB조회시 컬럼명을 동시에 보여줌
                     )
 
cur = con.cursor()

e_id = '6'
e_name ='6'
sex = '6'
addr = '6'

sql = f"""insert into emp
        values('{e_id}','{e_name}','{sex}','{addr}')"""
print(sql)
cnt = cur.execute(sql)
print("cnt",cnt)

con.commit()
cur.close()
con.close()




