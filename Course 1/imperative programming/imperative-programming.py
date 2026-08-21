import dis # import module for showing bytecode

# function finding the sum
def fun():
    s = 0
    for i in range(5, 16):
        s += i
    return s

# disassemble the bytecode of the function
dis.dis(fun)
