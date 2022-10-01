#!/usr/bin/python3

myList = ["banana", "cherry", "apple"]

print(myList)

item = myList[-3]

print(item)

print()
print()

for item in myList:
    print(item)


if "cherry" in myList:
    print("get it")
else:
    print("buggy")