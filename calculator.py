def calculator():
    print("Simple Calculator ")
    num1 = float(input("Enter a First Number: "))
    num2 = float(input("Enter Second Number: "))

    operation = input("Enter Operation: (+,-,*,/):")

    if operation  == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1/num2
        else:
            return "Error Division by zero"
    else:
        return "Invalid Operation"
    
    return f'Rusult : {result}'

print(calculator())


