# guessing number game

import random
y = 0

# Creat a function that will find a random int and set it equal to y 
# I set a value equal to 0 outside functions.
def ran(): 
	global y
	global random
	b = random.randint(1, 10)
	y = b


# Creat a function that will find a random int and set it equal to y
def start_instructions(): 
	global y
	x = int(input("pick a number between 1 and 10:"))
	if x > y:
		print("the number you picked is to high")
		start_instructions()
	if x < y:
		print("the number you picked is to low")
		start_instructions()
	if x == y:
		print("you are correct")

# I call the functions
ran()
start_instructions()
