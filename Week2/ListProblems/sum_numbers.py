#Week2 task2_4  sum_numbers.py

n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1
	
print(sum(numbers))
	