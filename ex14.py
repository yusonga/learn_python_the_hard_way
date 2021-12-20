from sys import argv
script, user_name = argv
prompt = '---' # or >> or ^ whatever symbol u like 

print(f"Hi{user_name}, i'm the {script}script")
print("i'd like to as you a few questions.")
print(f"Do u like me {user_name}?")
likes = input(prompt)

print(f"Where do u live {user_name}?")

lives = input(prompt)

print("what kind of computer do u have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.Nice.
""")
#input(prompt) === > + thing u want to add
