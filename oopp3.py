class Employee:
    num_of_emp = 0
    remain_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.remain_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.remain_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Alex', 50000)
emp_2 = Employee('John', 'Wick', 30000)

import datetime

my_date = datetime.date(2001, 12, 17)

print(Employee.is_workday(my_date))

# emp_str_1 = 'Obaidullah-Mansoor-50000'
# emp_str_2 = 'Muhammad-Arqam-50000'
# emp_str_3 = 'Mustatab-Safdar-50000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_2 = Employee.from_string(emp_str_2)
# print(new_emp_1.email)
# print(new_emp_1.pay)

# Employee.set_raise_amt(1.05)

# emp_1 = Employee('Corey', 'Alex', 50000)
# emp_2 = Employee('John', 'Wick', 30000)

# print(Employee.remain_amt)
# print(emp_1.remain_amt)
# print(emp_2.remain_amt)