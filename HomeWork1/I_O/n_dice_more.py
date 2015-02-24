#n_dice_more 

a = input ("Please enter the number of dice sides: ")
b = int(a)
#1st. roll
from random import randint
dice1 = randint (1, b)
print ("First Roll, you have thrown:")
print(dice1) 
#2nd. Roll
dice2 = randint (1, b)
print ("Second Roll, you have thrown:")
print(dice2)
#3rd. Roll
dice3 = randint (1, b)
print ("Third Roll, you have thrown:")
print(dice3)

sum = dice1 + dice2 + dice3
print ("Sum is:", '\n', sum)