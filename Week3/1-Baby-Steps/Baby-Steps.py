#Week3 Task1 Baby-Steps.py 

#1.Вдигане на квадрат

def square(x):
    return x ** 2


# 2. Factoriel

def factorial(n):
    result = 1
    start = 1

    while start <= n:
        result *= start
        start += 1

    return result


# 3. Колко елемента има в списък?

def count_elements(items):
    result = 0

    for item in items:
        result += 1

    return result


# 4. Дали елемент се намира в списък?

def member(x, xs):
    found = False
    
    for memb in xs:
        if x == memb:
            found = True
            break

    return found


# 5. Студенти с оценка над даден лимит

def grades_that_pass(students, grades, limit):
    result = []
    index = 0

    for grade in grades:
        student = students[index]
        
        if grade >= limit:
            result = result + [student]
        
        index += 1

    return result