history = []

while (x:= int(input("Enter non-negative integers: "))) > 0:
    if x not in history:
        history.insert(0,x)
    elif x in history:
        history.remove(x)
        history.insert(0,x)


print(history)