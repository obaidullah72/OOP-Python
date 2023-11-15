# program to illustrate public access modifier in a class

class Geek:

    # constructor
    def __init__(self, name, age):
        # public data members
        self.name = name
        self.age = age

    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.age)


# creating object of the class
obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.name)

# calling public member function of the class
obj.displayAge()
