class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
#class Child(Parent):
#def __init__(self, stuff):
#self.stuff = stuff
#super(Child, self).__init__()
#the same as the Child.sltered except setting some variables in the __init__before having the Parent initialize with its Parent.__init__
dad = Parent()
son = Child()

dad.implicit()
son.implicit()
#PARENT implicit()
#PARENT implicit()

dad.override()
son.override()
#PARENT override()
#CHILD override()
dad.altered()
son.altered()
#PARENT altered()
#CHILD altered()


#class SuperFun(Child, BadStuff):
#      pass
#make a class named SuperFun that inherits from the classed Child and BadStuff at the same time.
