n1=int(input("Enter 1st Number: "))
n2=int(input("Enter 2nd Number: "))
choice=input("Enter the Operation: + , - , * , / : ")
match choice:
    case '+':
        print("Addition of Two numbers: ",n1+n2)
    case '-':
        print("Substraction of Two numbers: ",n1-n2)
    case '*':
        print("Multiplication of Two numbers: ",n1*n2)
    case '/':
        print("Division of Two numbers: ",n1/n2)
    case _:
        print("Please choose correct option")