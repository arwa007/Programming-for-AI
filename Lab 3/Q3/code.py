import json

try:
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

    with open('myfile3.txt', 'w') as file: 
        file.write(json.dumps(myDict))

except FileNotFoundError:
    print("File not Found!")

except SyntaxError:
    print("Oops! Something is wrong with the syntax.")

else:
    print("Congrats! No errors.")

    with open('myfile3.txt') as file: 
        content = json.load(file)
    print(content)

finally:
    print("The program ends here.")
