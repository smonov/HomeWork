#Week2 Task2_3 only_evens.py

n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
OnlyEvensList = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1
 
for even in numbers:
    if even % 2 == 0:
        OnlyEvensList = OnlyEvensList + [even]
		
print("Count of evens is: ",len(OnlyEvensList))	    

for printEV in OnlyEvensList:
    print(printEV)
	
