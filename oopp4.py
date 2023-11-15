class Employee:
    num_of_emp = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang
        # Employee.__init__(self, first, last, pay)  other way to get a data

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees= employees

    def add_emp(self, employees):
        if employees not in self.employees:
            self.employees.append(employees)

    def rem_emp(self, employees):
        if employees in self.employees:
            self.employees.remove(employees)

    def print_emps(self):
        for employees in self.employees:
            print('-->', employees.fullname())


dev_1 = Developer('Corey', 'Alex', 80000, 'Python')
dev_2 = Developer('Test', 'Pass', 50000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Developer))

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.rem_emp(dev_1)
# mgr_1.print_emps()

# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)
# print(dev_1.email)
# print(dev_2.pay)
# print(dev_2.pro_lang)
# print(dev_2.pay)
# dev_2.apply_raise()
# print(dev_2.pay)