import random
import math

lwr = int(input("Enter the lower bound:- "))
upr = int(input("Enter the upper bound:- "))

x = random.randint(lwr,upr)
print("\n YOu have "+str(round(math.log(upr-lwr+1,2)))+"chances to predict the number")

count = 0

while count< math.log(upr-lwr+1,2):
	count += 1
	guess = int(input("Guess a number: "))
	if x==guess:
		print("Congratulations you found the corresct number in ",count,"th try")
		break
	elif x>guess:
		print("The number is small!")
	elif x<guess:
		print("The number is BIG!")
if count >=	math.log(upr-lwr+1,2):
	print("\n The number is ",str(x))
	print("You have exceeded the chances\n")
	print("Better Luck Next Time!!!!")
