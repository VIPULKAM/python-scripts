from unittest import TestCase, main
from employee import Employee
from emp_db import Employee_Db

emp1 = Employee_Db(63862, 'Vipul', 'Kadam')
emp2 = Employee_Db(157286, 'Lekshmi', 'Krishnan')
#emp = Employee_Db()


class Employeedb_Test(TestCase):

    def testinit(self):
        self.assertEqual(isinstance(emp1,Employee_Db) , True)
        self.assertEqual(isinstance(emp1,Employee) , True)
        self.assertEqual(isinstance(emp2,Employee) , True)
        self.assertEqual(isinstance(emp2,Employee_Db) , True)

    def test_emp_fullname(self):
        self.assertEqual(emp1.full_name, 'Vipul Kadam')
        self.assertEqual(emp2.full_name, 'Lekshmi Krishnan')

    def test_insert_db(self):
        emp1.insert_db()
        emp2.insert_db()
        self.assertEqual(emp2.get_emp_by_empid(157286), (157286, 'Lekshmi', 'Krishnan'))
        self.assertEqual(emp1.get_emp_by_empid(63862), (63862, 'Vipul', 'Kadam'))

    def test_delete_db(self):
        emp1.delete_db(63862)
        self.assertEqual(emp1.get_emp_by_empid(63862), None)
        self.assertEqual(emp2.get_emp_by_empid(157286), (157286, 'Lekshmi', 'Krishnan'))

if __name__ == '__main__':
    main()
