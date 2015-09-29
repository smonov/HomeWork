#Week2 task2_5 max_of_n.py

n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
CountBuffer = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1
	
for ListMember in numbers:
    if ListMember >= CountBuffer:
        biggest = ListMember
        
    else:   
        biggest = CountBuffer

print("Max is: " + str(biggest))


############################################################################
#Вярното ot Rado Решение е долу с малко мой поправки (Френдли юзер интерфейс)
############################################################################

#Week2 Task2_6  min_of_n.py

# Добавяме всички числа в numbers
# След което търсим най-голямото

n = input("Enter count of numbers: ")
n = int(n)

start = 0
numbers = []

while start < n:
    number = input("Enter number: ")
    number = int(number)
    
    numbers = numbers + [number]

    start += 1

# Най-голямото ни число е първото число в списъка
# След което обхождаме списъка
# И ако намерим по-голямо от това, което сме взели в началото
# Казваме, че новото current_max е това, което сме намерили
# Накаря, когато обходим списъка ще имаме най-голямото

current_max = numbers[0]

for number in numbers:
    if number > current_max:
        current_max = number

print("Max is: " + str(current_max))
