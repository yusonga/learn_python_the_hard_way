mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

#this goes in mystuff.py
def apple():
    print("I AM APPLES!")

import mystuff
mystuff.apple()


#this is just a variable
tangerine = "Living reflection of a dream"

mystuff.apple()
print(myttuff.tangerine)

mystuff['apple']# get apple from the dict
mystuff.apple() # get apple from the module
mystuff.tangerine  #same thing, it's just a variable


class MyStuff(object): # objects are like import

     def _init_(self):
        self.tangerine = "And now a thousand years between"
#__init__ function to initialize your newly created empty object
    def apple(self):
        print("I AM CLASSY APPLES!")
#self is empty object python made for you, you set self.tangerine to a asong lyric and then you've initialiezd this object.

thing = MyStuff()
thing.apple()
print(thing.tangerine)


#dict style
mystuff['apple']

#module style
mystuff.apples()
print(mystuff.tangerine)

#class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
