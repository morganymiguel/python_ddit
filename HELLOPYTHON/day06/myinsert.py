# STEP 1
import pymysql


# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python', charset='utf8',port =3305,
                        autocommit=True, # 결과 DB 반영 (Insert or update)
                      cursorclass=pymysql.cursors.DictCursor # DB조회시 컬럼명을 동시에 보여줌
                     )
 
cur = con.cursor()
sql = """insert into emp
        values(%s,%s,%s,%s)"""

cnt = cur.execute(sql,(5,5,5,5))
print("cnt",cnt)

con.commit()
cur.close()
con.close()




