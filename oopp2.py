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


print(Employee.num_of_emp)

emp_1 = Employee('Corey', 'Alex', 50000)
emp_2 = Employee('John', 'Wick', 30000)

print(Employee.num_of_emp)

# emp_1.remain_amt = 1.05
#
# print(emp_1.__dict__)

# print(Employee.remain_amt)
# print(emp_1.remain_amt)
# print(emp_2.remain_amt)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
