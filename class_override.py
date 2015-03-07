class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Hello, %s" % other.name
	print "test: %s" % self.name

class CEO(Employee):
    def greet(self, other):
        print "Get back to work, %s!" % other.name
	print "test2: %s" % self.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!
