print("Choose the mathematical operation you want to perform from the below list")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Quotient")
print("5. Remainder")
print("Enter two numbers")

while True:
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    print("a : ",a)
    print("b : ",b)
    num=int(input("Enter your choice : "))
    if (num==1):
            s=a+b
            print("Result of Addition is : ",s)
    elif (num==2):
            sub=a-b
            print("Result of Subtraction when a-b is done is : ",sub)
    elif (num==3):
            p=a*b
            print("Result of Multiplication is : ",p)
    elif (num==4):
            q1=a/b
            q2=b/a
            print("Quotient when a/b is : ",q1)
            print("Quotient when b/a is : ",q2)
    elif (num==5):
            r1=a%b
            r2=b%a
            print("Remainder when a is divided by b is : ",r1)
            print("Remainder when b is divided by a is : ",r2)
    else:
            print("Invalid choice")

    ch=input("Do you wish to continue?(Enter yes/no) ")
    if ch=="no":
       break
