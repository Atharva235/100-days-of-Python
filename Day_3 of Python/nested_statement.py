height=int(input("Enter your height in cm:\n "))
age=int(input("Enter your age:\n"))
bill=0

if height>=120:
   print("You can go on ride")
   if age>=18:
       bill=20
       print("You need to pay 20$")
   elif age<12:
       bill=10
       print("You need to pay 10$")
   else:
    bill=15
    print("You need to pay 15$")

   wants_photo=input("Do you want photo taken?Y or N\n")
   if wants_photo=="Y" or "y":
      bill+=3
   
   print(f"Your final bill is {bill}$")
else:
    print("You cannot go on ride")


#Exercise:
#BMI calculator

# height=float(input("Enter your height in cm:\n"))
# weight=float(input("Enter you weight in kg:\n"))
# bmi=(weight/height**2)
# print(bmi)

# if bmi<18.5:
#    print("You are under weight")
# elif bmi<25:
#    print("You have normal weight")
# elif bmi<30:
#    print("You are overweight")
# elif bmi<35:
#    print("You are obese")
# else:
#    print("You are clinically obese")