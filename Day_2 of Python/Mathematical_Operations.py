print(34+2)
print(34-2)
print(34*2)
print(34**2)
print(34/2)
print(34%2)


#order of priority:
# PEMDAS
# Parantheses()
# Exponents 2**2
# Multiplication 2*2
# Division 2/2
# Addition 2+2
# Substraction 2-2

print(3*3+3/3-3)
print(3*(3+3)/3-3)

#Exercise
#Body Mass index calculator:

weight=float(input("Enter your Weight in kg:\n"))
height=float(input("Enter your Height in m:\n"))

bmi=weight/height**2
print (int(bmi))
