from employee import Employee
from emp_db import Employee_Db

emp1 = Employee_Db(63862, 'Vipul', 'Kadam')
emp2 = Employee_Db(157286, 'Lekshmi', 'Krishnan')
#emp = Employee_Db()


def testinit():
    assert isinstance(emp1,Employee_Db) == True
    assert isinstance(emp1,Employee) == True
    assert isinstance(emp2,Employee) == True
    assert isinstance(emp2,Employee_Db) == True

def test_emp_fullname():
    assert emp1.full_name == 'Vipul Kadam'
    assert emp2.full_name == 'Lekshmi Krishnan'

def test_insert_delete_db():
    emp1.insert_db()
    emp2.insert_db()
    assert(emp2.get_emp_by_empid(157286) == (157286, 'Lekshmi', 'Krishnan'))
    assert(emp1.get_emp_by_empid(63862) == (63862, 'Vipul', 'Kadam'))
    emp1.delete_db(63862)
    emp1.delete_db(157286)
    assert(emp1.get_emp_by_empid(63862) ==  None)
    assert(emp2.get_emp_by_empid(157286) == (157286, 'Lekshmi', 'Krishnan'))

