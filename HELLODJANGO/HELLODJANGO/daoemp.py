import pymysql


class DaoEmp:
    def __init__(self):
        self.con = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8', port =3305)

        
        self.cur= self.con.cursor(pymysql.cursors.DictCursor)
    def mylist(self):
        sql ="SELECT e_id, e_name, sex, addr FROM emp"
        self.cur.execute(sql)
        
        
        mylist = self.cur.fetchall()
        return mylist
    
    
    
    def myone(self,e_id):
        sql =f"""SELECT e_id, e_name, sex, addr 
                FROM emp
                WHERE
                    e_id ='{e_id}' """
        self.cur.execute(sql)
        
        mylist = self.cur.fetchall()
        return mylist[0]      
    
    def myinsert(self, e_id,e_name, sex, addr):
        sql=f"""INSERT INTO emp (e_id, e_name, sex, addr)
                VALUES('{e_id}','{e_name}','{sex}','{addr}')"""
        
        
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
    def myupdate(self, e_id,e_name, sex, addr):
        sql=f"""UPDATE emp
                set E_NAME ='{e_name}', 
                    SEX='{sex}', 
                    ADDR='{addr}'
                WHERE E_ID ='{e_id}'
            """
        cnt = self.cur.execute(sql)
        self.con.commit()            
        return cnt
    
    def mydelete(self,e_id):
        sql =f"""
                DELETE FROM emp
                WHERE E_ID ='{e_id}'
            """
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
      
    def __del__(self):
        self.cur.close()
        self.con.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    emp = de.myone('7')
    print("emp",emp)
    cnt = de.myinsert('7','7','7','7')
    print("cnt",cnt)
    emp = de.myupdate(1,8,8,8)
    delete = de.mydelete(7)
    list = de.mylist()
    
    print("list",list)
        
    
    