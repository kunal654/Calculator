a=int(input("Enter your first number : "))
b=int(input("Enter your second number : "))
c=input("Select your operation from these : +,-,*,/,//,%,** : ")
if c == "+" :
    print("Sum of two number is : ", a+b)
elif c=="-" and a>b :
    print("Substraction between two number are",a-b)
elif c=="*":
     print("Multiplication of two number is : ", a*b)
elif c=="/" :
     print("Division of two number is : ", a/b)
elif c=="//":
      print("Floor division of two number is : ", a//b)
elif c=="%":
      print("Modulo of two number is : ", a%b)
elif c=="**":
      print("Exponential of two number is : ", a**b)
else:
     print("You enter a invalid operator")