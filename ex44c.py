class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")#
        super(Child, self).altered()#use super to get the parent.altered version
        #line 10 is aware of inheritance and will get the parent class for you
        #call super with arguments child and self then call the function altered on whatever it returns
        print("CHILD, AFTER PARENT altered()")
#parent.altered version of the function runs and that prints out the parent message.
dad = Parent()
son = Child()

dad.altered()
son.altered()
