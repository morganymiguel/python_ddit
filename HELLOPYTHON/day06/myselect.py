# STEP 1
import pymysql


# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python', charset='utf8',port =3305,
                        autocommit=True, # 결과 DB 반영 (Insert or update)
                      cursorclass=pymysql.cursors.DictCursor # DB조회시 컬럼명을 동시에 보여줌
                     )
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()
 
# STEP 4: SQL문 실행 및 Fetch
sql = "SELECT * FROM EMP"
cur.execute(sql)

# 데이타 Fetch
rows = cur.fetchall()
cols = cur.fetchall()

# STEP 5: DB 연결 종료
con.close()

print(rows)     # 전체 rows
print(cols)     # 전체 rows


