#Week2 Task2_2 read_n_numbers.py

n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1

print(numbers)

# Програмата създава списък от "n" на брой елемента
# и стойност на всеки елемент според въведената на есеки ред от потребителя.

