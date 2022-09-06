import pymysql

class DaoEmp:
    def __init__(self):
        self.con = pymysql.connect(host='localhost', user='root', password='python',
                               db='python', charset='utf8',port=3305) 
         
        
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
    
    def mylist(self):
        sql = "SELECT e_id,e_name,sex,addr FROM emp"
        self.cur.execute(sql)
        
        mylist = self.cur.fetchall()
        return mylist
    
    def myone(self,e_id):
        sql = f"""
            SELECT e_id,e_name,sex,addr 
            FROM emp
            WHERE
                e_id = '{e_id}'
            """
        self.cur.execute(sql)
        
        mylist = self.cur.fetchall()
        return mylist[0]
    
    def myinsert(self,e_id,e_name,sex,addr):
        sql = f"""insert into emp (e_id,e_name,sex,addr)
                 values ('{e_id}','{e_name}','{sex}','{addr}')"""
        cnt = 0
        try:
            cnt = self.cur.execute(sql)
            self.con.commit()
        except:
            cnt = 0
            
        return cnt
    
    def myupdate(self,e_id,e_name,sex,addr):
        sql = f"""
            update emp
            set
                e_name = '{e_name}',
                sex = '{sex}',
                addr = '{addr}'
            where
                e_id = '{e_id}'

        """
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt    
        
    def __del__(self):
        self.cur.close()
        self.con.close()
        

if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.myupdate('4','6','6','6')
    print("cnt",cnt)
