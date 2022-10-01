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

# Append element

myList.append("pinapple")

print(myList)

myList.insert(1, "blueberry")
print(myList)

myList.pop()
print(myList)

myList.pop(1)
# myList.sort()

print(myList)

myList.reverse()
print(myList)

myNumberList = [3, 65, 0, -3, 5, 8]

mySortedNumberLIst = sorted(myNumberList)

print(mySortedNumberLIst)

sliceList = mySortedNumberLIst[3:]

print(sliceList)

mySecondNumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

myThirdNumberList = list(range(0, 100, 2))

print(mySecondNumberList[::2])

print(myThirdNumberList)

# Tips to reverse list

reverseThirdNumberList = myThirdNumberList[::-1]

print(reverseThirdNumberList)


#Copy of list

