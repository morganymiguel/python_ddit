import pymysql
class DaoEmp:
    def __init__(self):
        self.con = pymysql.connect(localhost='localhost', user ='root', password = 'python', db ='python', charset = 'utf8', port = 3305)
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
        
    def emp(self):
        pass