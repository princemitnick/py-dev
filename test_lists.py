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

org_list = [1,2,3,4,5]

cpy_list = org_list

print(cpy_list)

cpy_list.pop()

print(org_list)


#Test copy with an integer variable

a = 4
b = a
print(a, b)

b = 6

print(a, b)


#Test copy with a string variable

a = "Mom"
b = a

print(a, b)

b = "Dad"

print(a, b)

#Test copy with tuple

t1 = (1, 2, 3, 4, 5, 6)

t2 = t1

print(t1)
print(t2)

t2 = (3,48,1,3)

print(t1)
print(t2)


#Test copy of list with copy() method and list() "object) and slicing [:]

myList = ["Jeremie", "Jacmel", "Cayes"]

myList1 = list(myList)
myList2 = myList1.copy()
myList3 = myList2[:]

print(myList)
print(myList1)

myList1.append("Gonaives")
myList2.append("Saint-Marc")
myList3.append("Mirebalais")
print(myList)
print(myList1)
print(myList2)
print(myList3)