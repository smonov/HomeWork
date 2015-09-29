#Week2 Task2_6  min_of_n.py

n = input("Enter count of numbers: ")
n = int(n)

start = 0
numbers = []

while start < n:
    number = input("Enter number: ")
    number = int(number)
    
    numbers = numbers + [number]

    start += 1

current_min = numbers[0]

for number in numbers:
    if number < current_min:
        current_min = number

print("Min is: " + str(current_min))
