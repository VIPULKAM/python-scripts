class Employee(object):

    def __init__(self, emp_id, first, last):
        self.emp_id = emp_id
        self.first = first
        self.last = last

    def __repr__(self):

        return f"{self.emp_id}:{self.first} {self.last}::{self.email}"

    def __str__(self):

        return "This is a Employee class which defines and stores employee metadata"

    @property
    def full_name(self):
        '''
        This method return first and last name of the employee
        '''
        return f"{self.first} {self.last}"

    @property
    def email(self):
        '''
        This method returns emailid of the employee
        '''
        return f"{self.first}.{self.last}@company.com"
