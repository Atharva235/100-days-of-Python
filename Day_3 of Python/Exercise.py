print("Welcome to the Pizza Shop")
size=input("What size pizza do you want? S,M,L\n")
add_pepperoni=input("Do you want peporroni? y or n\n")
extra_cheese=input("Do you want extra chesse? y or n\n")
bill=0

if size=="S":
    print("You will have to pay 15$ for small pizza")
    bill=15
    if add_pepperoni=="y":
        print("You will need to pay extra 2$")
        bill+=2
    if extra_cheese=="y":
        print("You will need to pay extra 1$")
        bill+=1
    print(f"Your total bill is {bill}$")
elif size=="M":
    print("You will have to pay 20$ for medium pizza")
    bill=20
    if add_pepperoni=="y":
        print("You will need to pay extra 3$")
        bill+=3
    if extra_cheese=="y":
        print("You will need to pay extra 1$")
        bill+=1
    print(f"Your total bill is {bill}$")
else:
    print("You will have to pay 25$ for large pizza")
    bill=25
    if add_pepperoni=="y":
        print("You will need to pay extra 3$")
        bill+=3
    if extra_cheese=="y":
        print("You will need to pay extra 1$")
        bill+=1
    print(f"Your total bill is {bill}$")
    