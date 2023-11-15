class Student:
    _name = None
    _rollno = None

    def __init__(self, name, rollno):
        self._name = name
        self._rollno = rollno

    def _printdetails(self):
        print('Roll No: ', self._rollno)

#     def privateaccess(self):
#         self.__printdetails()
#
#
# obj = Student('Obaidullah', 'BCSM-S20-006')
#
# obj.privateaccess()


class Employee(Student):

    def __init__(self, name, rollno):
        super().__init__(self, rollno)
        self._name = name

    def printdet(self):
        print('Name', self._name)
        self._printdetails()


obj = Employee('Obaidullah Mansoor', 'BCSM-S20-006')

obj.printdet()


