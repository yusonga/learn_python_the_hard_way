from sys import argv
from os.path import exists
#exists means retrun true if a file exists, return false if not
script, from_file, to_file = argv

print(f"Copying from{from_file} to {to_file}.")

#we could do these two on one line, how?
#in_file = open(from_file)
indata = open(from_file).read()
# use indata = open(from_file).read() will cause error at the end we dont need in_file.close()
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist?{exists(to_file)}")
print("Ready, hit RETURN to continue,CTRL-C to abort.")

input()

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
#in_file.close()

#echo "This is a test file." > test.txt  to make a sample filename
# cat test.txt to look at it
