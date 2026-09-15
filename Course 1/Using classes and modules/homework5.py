while (inp := input("my-calc: ")) != '':
    (num1, op, num2) = inp.split()
    num1 = float(num1)
    num2 = float(num2)

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(num1 / num2)
    else: print("Error: Invalid operator")