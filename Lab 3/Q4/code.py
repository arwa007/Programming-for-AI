try:
    name = input("Enter your name: ")
    age = (input("Enter your age: "))
    cnic = (input("Enter your CNIC number: "))
    salary = (input("Enter your salary: "))
    contact = (input("Enter your phone number: "))
    content = "Name: " + name + " Age: " + age + " Salary: " + salary 

    with open(r"newtext.txt", 'w') as file:
        file.write(content)
       
    contact = " Contact: " + contact
    with open(r"newtext.txt", 'a') as file2:
        file2.write(contact)

except FileNotFoundError:
    print("File not Found!")

except SyntaxError:
    print("Oops! Something is wrong with the syntax.")

except IOError:
    print("There was an error with I/O.")

else:
    print("Congrats! No errors.")

finally:
    print("The program ends here.")
