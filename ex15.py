from sys import argv

script, filename = argv
# get a filename
txt = open(filename)
#new command open
print(f"Here's your file{filename}:")
print(txt.read())
# a function on txt named read ,txt.read()says :hey txt! do your read command without parameters
#read the content of filename
#print(close(txt))
print("Type the filename again:")
file_again = input(">")
# > filename
txt_again = open(file_again)
#read the file again
print(txt_again.read())
#print(close(txt_again))  NameError: name 'close' is not defined
# print the content
#command are also called function and methods
# i dont know how to use close 
