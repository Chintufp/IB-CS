w = int(input("Enter weight: "))

def p(w):
    if w <=2:
        return 3
    elif w > 5:
        return 9 + 3 *(w - 5)
    else:
        return 3 + 2 *(w - 2)

print(f'The price for {w} kg is {p(w)} euros.')