# Week1 Task5.10 reverse_int.py

n = input("Enter a number: ")
n = int(n)

reversed_number = 0

while n != 0:
    digit = n % 10

    reversed_number = reversed_number * 10 + digit

    n = n // 10

print("The reversed number is: " + str(reversed_number))