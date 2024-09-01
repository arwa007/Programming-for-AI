#Write a python program that takes any two lists from user having same number of elements. Make a dictionary from these two lists in such a way that first element of first list 
# will be key and first element of second list will be its associated value and so on and print the result.
 
size = int (input("Enter the size of the list: "))
list1 = []
list2 = []
myDict = {}
temp = ''

print("Fill in List 1:")
for x in list(range(size)):
    temp = input(f"Enter value {x+1}: ") 
    list1.append(temp)

print("Fill in List 2:")
for x in list(range(size)):
    temp = input(f"Enter value {x+1}: ") 
    list2.append(temp)
   
for x in list(range(size)):
    myDict[list1[x]] = list2[x]

print(myDict)
