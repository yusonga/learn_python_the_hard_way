def chesse_and_crackers(chesse_count,boxes_of_crackers):
    print(f"you have{chesse_count}cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    #print("man that's enough for a party!")
    #print("get a blanket.\n")


print("we can just give the function numbers directly:")

chesse_and_crackers(20,30)
#call the function
print("OR,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#this two amount are global variables, should try to avoid to use it 
chesse_and_crackers(amount_of_cheese,amount_of_crackers)
#you can read the code out load ,like a language!!

print("we can even do math inside too:")
chesse_and_crackers(10+20, 5+6)

#10 version of run a function

print("and we can combine the two,variables and math:")
chesse_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
chesse_and_crackers(amount_of_cheese*3, amount_of_crackers*4)
chesse_and_crackers(6**8,99/33)
chesse_and_crackers(amount_of_crackers/5,amount_of_cheese%4)
#here even if i change the position of the amount_of_cheese ,it wont change anything at the end.
chesse_and_crackers(amount_of_crackers,amount_of_cheese)
chesse_and_crackers(-1,-3)
# i can use input to ask user for the numbers of chesse and ceackers.
