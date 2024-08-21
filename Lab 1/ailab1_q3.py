#Write a program to take an integerlist inputfrom user and count all the even numbersin thatlist and print the count.

my_list= []
count = 0

for var in list(range(5)):
    var = int(input("Enter Number\n"))
    my_list.append(var)

for var in list(range(5)):
    if my_list[var]%2 == 0:
        count += 1
        
print(count)