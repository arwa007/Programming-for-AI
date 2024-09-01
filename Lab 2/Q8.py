#Design a console based application for Converting different currency. You are required to ask user to choose input which currency you want to convert and then ask the amount. After that ask in which currency you want to convert. Then convert that currency into desired one...
#(Currency should includ Euro , Dollar, PkR, INR , and yen)

currIn = input("Enter the currency you possess (Euro , Dollar, PkR, INR , or yen): ")
currOut = input("Enter the currency you want (Euro , Dollar, PkR, INR , or yen): ")
amount = float(input("Enter your amount: "))

if currIn.lower() == 'euro' and currOut.lower() == 'pkr':
    amount *= 308.55
elif currIn.lower() == 'euro' and currOut.lower() == 'dollar':
    amount *= 1.11
elif currIn.lower() == 'euro' and currOut.lower() == 'inr':
    amount *= 92.67
elif currIn.lower() == 'euro' and currOut.lower() == 'yen':
    amount *= 161.74
elif currIn.lower() == 'dollar' and currOut.lower() == 'euro':
    amount *= 0.9
elif currIn.lower() == 'dollar' and currOut.lower() == 'pkr':
    amount *= 278.89
elif currIn.lower() == 'dollar' and currOut.lower() == 'inr':
    amount *= 83.89
elif currIn.lower() == 'dollar' and currOut.lower() == 'yen':
    amount *= 146.21
elif currIn.lower() == 'pkr' and currOut.lower() == 'euro':
    amount *= 0.0032
elif currIn.lower() == 'pkr' and currOut.lower() == 'dollar':
    amount *= 0.0036
elif currIn.lower() == 'pkr' and currOut.lower() == 'inr':
    amount *= 0.3
elif currIn.lower() == 'pkr' and currOut.lower() == 'yen':
    amount *= 0.52
elif currIn.lower() == 'inr' and currOut.lower() == 'euro':
    amount *= 0.011
elif currIn.lower() == 'inr' and currOut.lower() == 'dollar':
    amount *= 0.012
elif currIn.lower() == 'inr' and currOut.lower() == 'pkr':
    amount *= 3.32
elif currIn.lower() == 'inr' and currOut.lower() == 'yen':
    amount *= 1.74
elif currIn.lower() == 'yen' and currOut.lower() == 'euro':
    amount *= 0.0062
elif currIn.lower() == 'yen' and currOut.lower() == 'dollar':
    amount *= 0.0068
elif currIn.lower() == 'yen' and currOut.lower() == 'pkr':
    amount *= 1.91
elif currIn.lower() == 'yen' and currOut.lower() == 'inr':
    amount *= 0.58
else:
    print("Your input is invalid.")

print(f"Converted amount: {amount} {currOut}")
