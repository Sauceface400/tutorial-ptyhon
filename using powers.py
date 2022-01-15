def cube(num):
    return num*num*num

result = cube(5)
print(result)

squareroot = int(input("place a number: "))
roots = input("place a squareroot or cuberoot: ")

if roots == "2":
    print(squareroot*squareroot)
elif roots == "3":
    print(squareroot*squareroot*squareroot)
else:
    print("out of range")