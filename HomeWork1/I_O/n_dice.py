#n_dice task
a = input ("Please enter the number dice's sides: ")
b = int(a)
from random import randint
dice = randint (1, b)
print ("You have thrown:")
print(dice)