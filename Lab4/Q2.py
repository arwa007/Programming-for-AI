#Two lists are given : list1 = ["Hello ", "take "] , list2 = ["Dear", "Sir"]
#Concatenate these two lists like this : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Using a nested loop inside list comprehension
result = [x + y for x in list1 for y in list2]

print(result)
