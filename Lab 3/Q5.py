#Take input from user below dictionary having name and age pair. Save this dictionary in json file. 
# Now load this json file and Print name of person having maximum age and also
# print if anyone has the same age by making logic yourself without using any library:

import json
try:
    size = int(input('Enter the amount of names you want to enter: '))
    my_dict = {}
    readDict = {}
    max = -1

    for x in range(1, size+1):
        name = input(f'Enter name {x}: ')
        age = int(input("Enter Age: "))
        my_dict[name] = age

    with open ('nameAge.txt', 'w') as file:
        json.dump(my_dict, file)

    with open ('nameAge.txt', 'r') as file2:
        readDict = json.load(file2)

    for name, age in readDict.items():
        if age > max:
            max = age
    print("Max age is:", max)

    print("Duplicate Ages are: ")
    age_count = {}
    for age in readDict.values():
        age_count[age] = age_count.get(age, 0) + 1

    duplicates_found = False
    for age, count in age_count.items():
        if count > 1:
            print(f"Age {age} appears {count} times")
            duplicates_found = True

    if not duplicates_found:
        print("No duplicate ages found.")

except FileNotFoundError:
    print("File not Found!")

except ValueError:
    print("You entered the wrong value.")

else:
    print("No errors found.")

finally:
    print("Program ends here.")
