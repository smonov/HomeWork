#Week1 If_Elif task2 dice game

sides = input("Enter the dice sides number: ")
sides = int(sides)

P1 = input("Enter the name of the lucky Guy1:")
P2 = input("Enter the name of unlucky Guy2:")

from random import randint

thrown1 = input("P1, Press space and then enter to throw")  

if thrown1 == " ": 
	luckyDice = randint (1, sides)
	print (P1, "Your result is:", luckyDice)
else:
	print ("You have pressed wrong key")
	
thrown2 = input("P2, Press space and then enter to throw")  

if thrown2 == " ": 
	unluckyDice = randint (1, sides)
	print (P2, "Your result is:", unluckyDice)
else:
	print ("You have pressed wrong key")
	
if luckyDice < unluckyDice:
	print (P2, "WIN!")
elif luckyDice > unluckyDice:
	print (P1, "WIN!")
elif luckyDice == unluckyDice:
	print ("Result is DRAW!") 
