#Week2 Task3.4 is_perfect2.py

n = input("Enter n: ")
n = int(n)

divisors_sum = 0

start = 1
end = n - 1

while start <= end:
    if n % start == 0:
        divisors_sum += start

    start += 1

if divisors_sum == n:
    print("Number is perfect")
else:
    print("Number is not perfect")