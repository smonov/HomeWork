#Week2 Task2.9 sorted_names.py

n = input("Enter count of names: ")
n = int(n)

count = 1
names = []

while count <= n:
    name = input("Enter name: ")
    names = names + [name]

    count += 1

names = sorted(names)

for name in names:
    print(name)
