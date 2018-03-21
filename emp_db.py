import sqlite3
from employee import Employee

class Employee_Db(Employee):

    def __init__(self, emp_id, first, last):
        self.emp_id = emp_id
        self.first = first
        self.last = last
        super().__init__(self.emp_id, self.first, self.last)
        self.conn = sqlite3.connect(':memory:')
        self.cur = self.conn.cursor()
        with self.conn:
            self.cur.execute("""CREATE TABLE employees(
                emp_id,
                first text,
                last text)
                """)

    def __repr__(self):
        pass

    def insert_db(self):
        with self.conn:
            self.cur.execute("insert into employees values(:emp_id, :first, :last)", {'emp_id':self.emp_id, 'first':self.first, 'last':self.last})

    def get_emp_by_empid(self, emp_id):
        self.cur.execute("select emp_id from employees where emp_id =:emp_id",{'emp_id': emp_id})
        self.t = self.cur.fetchone()
        self.emp_id, = self.t
        return self.emp_id


