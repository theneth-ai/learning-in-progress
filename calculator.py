num1=float(input("Number first number: "))
opt=input("Enter the operator: ")
num2=float(input("Number second number: "))
result=None
match opt:
    case "+":
        result=num1+num2
    case "-":
        result=num1-num2
    case '*':
        result=num1*num2
    case '/':
        if num2==0:
            print("Zero division error!")
        else:
            result=num1/num2
    case _:
        print("Invalid operator!")
if result is not None:
    print(f"{num1}{opt}{num2}=", result)
