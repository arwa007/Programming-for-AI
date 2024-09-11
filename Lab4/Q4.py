# Make a class "Employee". Create "get_data" function inside this class that will take input from user employee name ,monthly salary and percentage of tax.
# Create another function "Salary_after_tax" that will deduct 2% tax on monthly salary and return remaining salary.
# There will be another function of "update_tax_percentage" inside this class that will change tax percentage (for example initially if it was taken 2% then you may update it to 3%).
# Now again salary will be calculated based on this new tax percentage.

class employee:
    def getData(self) :
        self.name = input("Enter Employee Name: ")
        self.salary = float(input("Enter Employee Salary: "))
        self.perc = int(input("Enter percentage of tax: "))
    
    def salaryAfterTax(self):
        return self.salary*(1-(self.perc/100))
    
    def updateTaxPerc(self, newPerc):
        self.perc = newPerc


e1 = employee()
e1.getData()

print(f"Salary after tax is {e1.salaryAfterTax()}")

e1.updateTaxPerc(newPerc=3)

print(f"Salary after updated tax is {e1.salaryAfterTax()}")

        
