print("Welcome to the Treasure Island!!")
print("Your mission is to find treasure")
direction=input("Enter in which direction you want to go left or right\n").lower()

if direction=="right":
    print("You lost game over")
if direction=="left":
       swim= input("Enter swim or wait\n").lower()
       if swim=="swim":
           print("You lost game over")
       if swim=="wait":
               door=input("Which door blue,red,yellow\n").lower()
               if door=="yellow":
                   print("Congratulation you win")
               else:
                   print("You lost Game Over")
else:
     print("Game Over")