print("*****Simple Calculator*****")
n1 = float(input("Enter first number here: "))
n2 = float(input("Enter second number here: "))
print ("""
Enter 1 for Addition of two numbers
Enter 2 for Subtraction of two numbers
Enter 3 for Multiplication of two numbers
Enter 4 for Division of two numbers""")

ch = int(input("Enter a number between 1 to 4 to perform the desired operation: "))

if ch == 1:
    sum = n1+n2
    print ("Addition of",n1,'and',n2,"is:",sum)
elif ch == 2:
    sub= n1-n2
    print ("Subtraction of",n1,'and',n2,"is:",sub)
elif ch == 3:
    mul= n1*n2
    print ("Multiplication of",n1,'and',n2,"is:",mul)
elif ch == 4:
    div= n1/n2
    print ("Division of",n1,'and',n2,"is:",div)
else:
    print ("Enter valid Input")
