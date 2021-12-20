class Parent(object):

    def implicit(self):
        print("PANRENT implicit()")

class Chile(Parent):
    pass
#pass is how you tell python that you want a empty block
dad = Parent()
son = Chile()

dad.implicit()
son.implicit()
