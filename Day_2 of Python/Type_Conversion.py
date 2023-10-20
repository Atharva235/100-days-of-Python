num_char=len(input("Enter your name:"))
# print("Your name has"+ num_char + "characters.")
#This code will note be executed as num_char is a int data type while other are string datatype.

#Another way would be we will convert the num_char into string like this:
str_conversion=str(num_char)

#Now we can concatenate it
print("Your name has " + str_conversion + " characters.")

#We can convert string into int like this:
a="1235"
str_num=int(a)
print(str_num)

# We can use type() function to get what is the datatype of the varaible is
print(type(a))


#Exercise:
userNum=input("Enter your two digit number:")

firstNum=int(userNum[0])
secondNum=int(userNum[1])

add=print(firstNum + secondNum)