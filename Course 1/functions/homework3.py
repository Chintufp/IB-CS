def read_ints():
    ints =[]
    while (x := input("Enter a integer: ")) !='' :
        ints.append(int(x))
    return ints
    
print(read_ints())