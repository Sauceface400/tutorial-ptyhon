num = int(input("Put any number here: "))
symbols = input("put a symbol here: ")
anothernum = int(input("Put any number here: "))

if symbols == "+":
    print(num + anothernum)
elif symbols == "-":
    print(num - anothernum)
elif symbols == "x":
    print(num * anothernum)
elif symbols == "/": 
    print(num / anothernum)
elif symbols == "%":
    print(num % anothernum)

t = ["list","hack","far"]
t.pop()
print(t.index())
#========================EXAMPLE'S========================================