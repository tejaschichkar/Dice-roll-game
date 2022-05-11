import random
import time

d1 = (1,2,3,4,5,6)
d2 = (6,5,4,3,2,1)

roll_dice = input("Do you want to roll the dice y/n \n")

p1 = random.choice(d1)
p2 = random.choice(d2)
s = p1 + p2

def roll():
    if roll_dice == "y":
        print("Rolling the dices")
        print("The values are...")
        print(p1)
        print(p2)
        print(f"The sum of two dices is {s}")
    if roll_dice == "n":
        print("Didn't rolled dices")
        
roll()
