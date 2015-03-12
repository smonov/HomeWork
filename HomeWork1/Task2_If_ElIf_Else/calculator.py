#Week1 Task 2.3 Calculator

a = input ("Enter a: ")
a = int(a)
b = input ("Enter b: ")
b = int(b)

opr = input("Enter operator: ")

if opr == "+":
    result = ( a + b )
    print ("Result is: ", result) 
elif opr == "-":
    result = ( a - b )
    print ("Result is: ", result)
elif opr == "*":
    result = ( a * b )
    print ("Result is: ", result)
elif opr == "/":
    result = ( a / b )
    print ("Result is: ", result)
else:
        print ("Unsupported operation")


        
