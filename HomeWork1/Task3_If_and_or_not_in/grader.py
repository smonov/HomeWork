#Week1 Task 3.3 "Grader"

n = input("Въведете името на ученика: ")
r = input("Въведете резултата от теста: ")
r = int(r)

if r <= 50:
	print(n," има двойка")
elif r > 50 and r < 61:
	print(n," изкара тройка")
elif r > 60 and 71 > r:
	print(n,"има Добър 4")
elif r > 70 and r < 81:
	print(n,"има Много Добър 5")
elif r > 80 and r < 100: 	
	print(n,"има Отличен 6")
else:
	print(n,"има Много Отличен 7")
