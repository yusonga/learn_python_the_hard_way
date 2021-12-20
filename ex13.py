
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
scr=input("name of the file")
fir = input("first variable")
sec = input("sec variable")
thi = input("third")
#input 之后是（） 并不是{}
print(f"this {scr} is called:", script)
print(f"your {fir} variable is:", first)
print(f"your {sec} variable is:", second)
print(f"your {thi} variable is:", third)
#如果想要print出input的内容 需要在前面加上一个f！！！！
#python3.9 ex13.py apple orange grape-fruit
#script ==ex13.py fir=app sec=ora thi=grape
#the diffrence between argv and input() user在那里需要input 如果需要在comandline input ，就用argv 如果需要input在运行的时候打出来 就用input
