class myDecorator(object):
    def __init__(self,func_name):
	self.func_name = func_name    

    def __call__(self):
        print "Enter"
	self.func_name()
        print "Leave"

@myDecorator
def func1():
    print "Hello~~"

func1();
