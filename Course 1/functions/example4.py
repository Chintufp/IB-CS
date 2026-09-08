def read_floats(n):
    return [float(input(f'input value {x+1} out of {n}: ')) for x in range(n)]

print(read_floats(2))