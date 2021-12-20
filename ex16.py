from sys import argv

script, filename = argv

print(f"We're going to erase{filename}.")
print("If you dont watch that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,"w")
# why we use a w?  w is a string with character in it. use w means open this file in wirte mode ,r for read, a for append
#open(filename) open in read mode.
print("Truncating the file. Goodbye!")
target.truncate()

print("Now i'm going to ask you for thress lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# repeat too much ,how to simplify it?
#target.write(f"""
#{line1}
#\n
#{line2}
#\n 
#{line3}
#\n
#"""}
print("And finnaly, we close it.")
target.close()
# now i use read to read the file
txt = open(filename)

print(txt.read())
