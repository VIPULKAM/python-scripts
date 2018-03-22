from employee import Employee

emp1 = Employee(63862, 'Vipul', 'Kadam')


def testinit():
        assert(isinstance(emp1,Employee) == True)
        assert(emp1.first == 'Vipul')
        assert(emp1.last == 'Kadam')
        assert(emp1.emp_id == 63862)

def test_emp_fullname():
        assert(emp1.full_name == 'Vipul Kadam')

def test_emp_email():
        assert(emp1.emp_email == 'Vipul.Kadam@company.com')

def test_emp_repr():
        assert(emp1.__repr__() == '63862:Vipul Kadam::Vipul.Kadam@company.com')

