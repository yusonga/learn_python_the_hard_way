types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"i said: {x}")
print(f"i also said:'{y}'")
# a string put inside a srting 
hilarious = False
joke_evaluation = "isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious)) # format hilarious = false so here we have a answer for the joke
#isn't that joke so funny?! false
w = "this is the left side of ..."
e = "a string with a right side."

print(w + e)
