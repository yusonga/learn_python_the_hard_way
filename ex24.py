print("let's practice everything.")
print("you\'d need to know \'boit escapes with \\ that do:")
print("\n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\twhere there is none.
"""

print("-----------")
print(poem)
print("-----------")

five = 10 -2 + 3 -6
print(f"This should be five:{five}")

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/1000
    return jelly_beans,jars,crates



start_point = 10000
beans,jars,crates = secret_formula(start_point)
#jelly_beans and beans wont have any influrence 
#remember that this ia ianother way to format a string
print("with a starting point of: {}".format(start_point))
#its just like with and f"" string
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("we cans also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format strings
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))
