"""
user = input("Enter: ")
message = "like this baby {}".format(user)

print(message)

sentence = "go girl i know it".split()

for s in sentence:
    print(sentence)j

x = "1234567"
print(x[::3])#the last one is a step which is moving 3 numbers at a time

jobs = {"name":"fabion","ocupation":["engineer","economist","IT"]}

print(["ocupation"][1])

person = {"a":1,"b":2}

try:
    #print(person["kkkk"])
    print(10/0)
except KeyError:
    print("exception has occured in the code")
except ZeroDivisionError:
    print("no value")
finally:
    print("the code has been called")


data = 1 
while data <= 10:
    print(data)
    data = data + 1

data = [1,0,2,4,5,10]
a = 1
for x in data:
    if x == 0:
        continue
    a = a * x
print("the value is {}".format(a))

data = [1,2,3,4,0,10]

search = 0 

for j in data:
    if search == j:
        print("found it lol")
    else:
        print("another one")
        break
"""

def add(x,y):
    result = x + y
    return result
result = add(10,20)
print(result)