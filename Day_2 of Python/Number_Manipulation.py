print(round(8/3))#It will round-off
print(round(8/3,2))#It will round-off upto 2 digits we can use to specify how much we want to round-off upto.


#user scores a point
score=0
score=+1
print(score)

# f-strings
print(f"Your score is {score}")

#Exercise:
age=int(input("Enter your age:"))
years_remaining=90-age
days=years_remaining*365
weeks=years_remaining*52
months=years_remaining*12
print(f"You have {days} days,{weeks} weeks,{months} months left.")