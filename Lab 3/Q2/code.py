try:
    with open (r"myfile2.txt", "r+") as file:
        content = file.read()
        

except FileNotFoundError:
    print("File not Found!")
else:
    print("File Found!")
    search = input("Enter the word you want to search for: ")
    replace = input("Enter the word you would like to replace with: ")

    content2 = content.replace(search, replace)
    
    with open (r"myfile2.txt", "w") as file:    
        file.write(content2)
        
    with open (r"myfile2.txt", "r") as file:
        content = file.read()
        print(content)
    
finally:
    print("Program ends here.")
