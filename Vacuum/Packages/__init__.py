s = "hello"

i = iter(s)
while i.__next__():
    print(s)