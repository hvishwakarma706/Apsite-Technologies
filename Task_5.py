print('************ CALCULATOR PROGRAM **************')
num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))
op = input("Enter the operand : ")

match op:
    case '+': print(num1 + num2)
    case '-': print(num1 - num2)
    case '*': print(num1 * num2)
    case '/': print(num1 / num2)
    case _: print("Invalid operand")
