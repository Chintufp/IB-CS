n = int(input("Enter a positive integer: "))

if n >0:
    count = 1
    while n > 1:
        count *= n
        n -=1

    print(f"Factorial is {count}")
else:
    print("N MUST be POSITIVE !!!")