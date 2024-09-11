# Make a class "Student"and make a function "Print_biodata" inside it. Pass name and age of student to constructor. 
# Now access "Print_biodata" function using object to print name and age of student.

class student:
    name = ''
    age = 0
    def __init__ (self, name, age):
        student.name = name
        student.age = age
    
    def printBioData(self):
        print(f"Name: {student.name}")
        print(f"Age: {student.age}")
        
s1 = student("Arwa", 21)
s1.printBioData()
