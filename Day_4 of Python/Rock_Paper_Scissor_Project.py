import random
user_input=int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissor\n"))
if user_input==0:
    print("Your choice is Rock")
elif user_input==1:
    print("Your choice is Paper")
elif user_input==2:
    print("Your choice is scissor")
else:
    print("You chose invalid input please try again")

computer=["Rock","Paper","Scissor"]
computer_choice=random.choice(computer)
print(f"Computer choice is {computer_choice}")

if computer_choice=="Rock" and user_input==1:
    print("You Won")
elif computer_choice=="Rock" and user_input==2:
    print("Computer won")
elif computer_choice=="Rock" and user_input==0:
    print("It's a tie")
elif computer_choice=="Paper" and user_input==0:
    print("Computer won")
elif computer_choice=="Paper" and user_input==2:
    print("You won")
elif computer_choice=="Paper" and user_input==1:
    print("It's a tie")
elif computer_choice=="Scissor" and user_input==0:
    print("You won")
elif computer_choice=="Scissor" and user_input==1:
    print("Computer won")
elif computer_choice=="Scissor" and user_input==2:
    print("It's a tie")
else:
    print("Invalid input try again")
