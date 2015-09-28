#Week1 Task5.13 factorial.py

n = input("Enter a number: ")
n = int(n)

start = 1
# Тук ще пазим резултата
product = 1

while start <= n:
    product = product * start
    start = start + 1

print(product)