##Animal is-a object(yes, sort of confusing)llok at the extra credit
class Animal(object):
    pass

## dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ##??
        self.name = name

## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##??
        self.name = name
## person  is -a object
class Person(object):

    def __init__(self, name):#__init__是一个特殊的初始方法可以预设重要的变量
        ## person has-a name
        self.name = name

        #person has-a pet of some kind
        self.pet = None
#self.pet attribute of that clss is set to a default of none.

## is a
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what's this strang magic?
        super(Employee, self).__init__(name)
        ## Employee has- a salary of some kind
        self.salary = salary

## is a
class Fish(object):
    pass

## is a
class Salmon(Fish):
    pass

## is a
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## mary has a pet
mary.pet = satan

## frank is a Employee
frank = Employee("Frank", 120000)

## frank has a pet named rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
