#Week2 Task2.7 avg.py

n = input("Enter n: ")
n = int(n)

start = 0
numbers = []

while start < n:
    number = input("Enter number: ")
    number = int(number)
    
    numbers = numbers + [number]

    start += 1


total_sum = 0
count_numbers = len(numbers)

for number in numbers:
    total_sum += number

avg = total_sum / count_numbers

print("Avg is: " + str(avg))
