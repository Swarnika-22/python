import random as rm
num=rm.randint(1,5)
count=0
for i in range(1,4):
    user_num=int(input("Guess the no [1-5]:"))
    count += 1
    if num == user_num:
        print("Good guess........")
    else:
        print("Sorry, try again")
    if count > 3:
        print("You have crossesd limit")