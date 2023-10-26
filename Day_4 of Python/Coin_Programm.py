import random

test_seed=int(input("Create a seed number: "))
random.seed(test_seed)

radnom_side=random.randint(0,1)
if radnom_side==1:
    print("Heads")
else:
    print("Tails")
    