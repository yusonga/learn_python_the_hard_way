#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")
#*args (asterisk args)  *tells python to take all the arguments to the fonction and then put them in args as a list,its like argv .its not normally used too often 
    #ok,that*args is actually pointless,we can just do this
def print_two_again(arg1,arg2):
        print(f"arg1:{arg1},arg2:{arg2}")

        #this just takes one argument
def print_one(arg1):
    print(f"arg1:{arg1}")

#this one takes no arguments
def print_none():
    print("i got nothin'.")


print_two("yu","song")
print_two_again("yu","song")
print_one("First!")
print_none()
