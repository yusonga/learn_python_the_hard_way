tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm spli\non a line."
backslash_cat = "I'm\\a\\cat."
#	I'm tabbed in.
#I'm spli
#on a line.
#I'm\a\cat.
# \t means space before
fat_cat = """
I'll do a list:
\t*Cat food
\t*Fishies
\t*Catnip\n\t*Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#""" is correct "  " " will cause error
#single-quote'  when u have a double quote inside
#and double-quote" when u have a single quote inside
# "i "understand" joe" will get confused by python
#one way of solution "i am 6'2\" tall." escape double quote inside string
# 2 solution 'i am 6\'2" tall.' escape single-quote inside string
# 3 solution by using """ """ triple-quotes
