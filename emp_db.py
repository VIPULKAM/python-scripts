import sqlite3
from employee import Employee

class Employee_Db(Employee):

    def __init__(self, emp_id, first, last):
        self.emp_id = emp_id
        self.first = first
        self.last = last
        super().__init__(self.emp_id, self.first, self.last) # Calling super class constructor

        # Intializing sqllite database in memory

        self.conn = sqlite3.connect(':memory:')
        self.cur = self.conn.cursor()
        with self.conn:
            self.cur.execute("""CREATE TABLE employees( emp_id, first text, last text)""")

    #def __repr__(self):
    #    return super().__repr__()

    def insert_db(self):
        with self.conn:
            self.cur.execute("insert into employees values(:emp_id, :first, :last)", {'emp_id':self.emp_id, 'first':self.first, 'last':self.last})

    def delete_db(self, emp_id):
        with self.conn:
            self.cur.execute("delete from employees where emp_id =:emp_id", {'emp_id':emp_id})

    def get_emp_by_empid(self, emp_id):
        self.cur.execute("select * from employees where emp_id =:emp_id",{'emp_id': emp_id})
        return self.cur.fetchone()


