people = 20
cars = 20
trucks = 20


if people < cars or trucks < cars:
    print("we should take the cars.")
elif people > cars and trucks > cars:
    print("we should not tale the cars.")
else:
    print("We can't decide.")


if cars < trucks:
    print("Too many trucks.")
elif cars > trucks:
    print("Maybe we could take the trucks.")
else:
    print("we can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
