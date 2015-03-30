# Week1 task4.3 user_to_user

a = input("Enter a: ")
b = input("Enter b: ")
a = int(a)
b = int(b)
	
if a == b:
	print ("Both numbers are equal! There is nothing to count between them.:)")
elif a >= b:	
	while a >= b:
		print(b)
		b = b + 1
else:
	while a <= b:
		print(a)
		a = a + 1
###
### Във условието на задачата не се изисква обратно броене ### затова не се случва и във решението. Споменвам го 
### защото във даденото решение програмата брои и на обратно.
####