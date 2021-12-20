from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
# read the file
def rewind(f):
    f.seek(0)
#seek(0) move the file ro the 0 byte in the file
#every time u do f.seek(0), you're moving to the strast of the file.
#seek移动文件的读取指针到指定位置 有三种模式 f.seek(0)表示移动到文件头位置
def print_a_line(line_count, f):
    print(line_count, f.readline())
#inside readline()is code that scans each byte of the file until it fins a \n charachter then stops reading the file to return what it foubnd so far
#f.readline reading a line from the file and moving the read head to right after \n that ends that line
current_file = open(input_file)
# here current_file = file
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)
#
print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)
# line_count = current_line
#print each line of the file
current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)
# one error here its current_line not current_file
#the readline() function returns the \n thats in the file at the end of that line.
#add a end ="" adt the end of print calls to avoid adding double \n every line
