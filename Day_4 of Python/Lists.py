states=["Maharashtra","Gujrat","Rajasthan","Haryana"]
print(states[0])#It will print only first state.
#We can change the state by following synatx:
states[2]="Kerala"
print(states)

#Lists are mutable

#To add new item to list we use append function:
states.append("Punjab")
print(states)

#To remove an item from the list we use remove function and to remove all items we use clear function:
states.remove("Punjab")
states.clear()

#To reverse we use reverse function:
states.reverse()
print(states)

#split function:It will seperate each word with specified symbol here it is comma.
string="Hello,world,from,me" 
op=string.split(",")
print(op)

#Exercise:
# Who will pay the bill:
import random
test_seed=int(input("create a seed number:"))
random.seed(test_seed)

names=input("Give me names ,seperated by comma\n")
names_cv=names.split(",")
print(names_cv)
print(len(names_cv))
random_name=random.randint(0,len(names_cv))
print(random_name)
who_will_pay=names_cv[random_name]
print(f"{who_will_pay} will pay the bill for today's dinner")

#There is a random.choice function which help us to choice a random item from the list
#another way of writing above code will be very simple:
# other_way=print(random.choice(names_cv))
# print(f"{other_way} will pay the bill for today's dinner")