print("Welcome to the Tip Calculator")
bill=float(input("Enter the bill amount:\n"))
tip=int(input("Enter tip percent amount:\n"))
people=int(input("Enter no of people you want to split with:\n"))

tipPercent=tip/100
tipBill=bill*tipPercent+bill
print(tipBill)

each_personBill=tipBill/people
print(f"Each person should pay {each_personBill}")