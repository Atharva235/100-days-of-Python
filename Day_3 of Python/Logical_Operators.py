#Logical operators :

#AND operator:It returns true if both the given conditions are true for eg:
a=12
print(a>10 and a<15)

#or opeartor:It returns true if any one condition is true for eg:
a=12
print(a>20 or a<15)

#not operator:It returns the opposite value if value is true it returns false and vice versa for eg:

# height=int(input("Enter your height in cm:\n "))
# age=int(input("Enter your age:\n"))
# bill=0

# if height>=120:
#    print("You can go on ride")
#    if age>=45 and age<=55:
#       print("You can go on ride for free")
#    elif age>=18:
#        bill=20
#        print("You need to pay 20$")
#    elif age<12:
#        bill=10
#        print("You need to pay 10$")
#    else:
#     bill=15
#     print("You need to pay 15$")

#    wants_photo=input("Do you want photo taken?Y or N\n")
#    if wants_photo=="Y" or "y":
#       bill+=3
#    print(f"Your final bill is {bill}$")
# else:
#     print("You cannot go on ride")



#Exercise:
#Love calculator:
print("Welcome to love calculator!!")
person1=input("What is your name?\n")
lower1=person1.lower()
person2=input("What is there name?\n")
lower2=person2.lower()
love=lower1+lower2

t=love.count("t")
r=love.count("r")
u=love.count("u")
e=love.count("e")
true= t + r + u + e
 
l=love.count("l")
o=love.count("o")
v=love.count("v")
e=love.count("e")
love= l + o + v + e
 
love_score=str(true)+str(love)
int_score=int(true)+int(love)

if int_score<10 or int_score>90:
    print(f"Your score is {love_score},you go together like coke and mentos")
elif int_score>=40 and int_score<=50:
    print(f"Your score is {love_score},you are alright together")
else:
    print("Your score is "+love_score)