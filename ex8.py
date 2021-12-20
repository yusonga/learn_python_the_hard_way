formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try your",
    "own here here",
    "maybe a poem",
    "or a song about fear"
))
#formatter and fomat are deffrent,call it format function its a command line named formatter
#"one" are diffrent from True and 1, need to use str 
