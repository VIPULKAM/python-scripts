from unittest import TestCase, main
from employee import Employee

emp1 = Employee(63862, 'Vipul', 'Kadam')


class Employee_Test(TestCase):

    def testinit(self):
        self.assertEqual(isinstance(emp1,Employee) , True)
        self.assertEqual(emp1.first, 'Vipul')
        self.assertEqual(emp1.last, 'Kadam')
        self.assertEqual(emp1.emp_id, 63862)

    def test_emp_fullname(self):
        self.assertEqual(emp1.full_name, 'Vipul Kadam')

    def test_emp_email(self):
        self.assertEqual(emp1.emp_email, 'Vipul.Kadam@company.com')

    def test_emp_repr(self):
        self.assertEqual(emp1.__repr__(), '63862:Vipul Kadam::Vipul.Kadam@company.com')

if __name__ == '__main__':
    main()
