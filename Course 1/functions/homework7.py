#1
def iterate(f,x,n):
    if n == 0:
        return x
    else:
        return iterate(f, f(x), n-1)

def f(x):
    return 0.5 * (x + 2/x)

# print(iterate(f, 1, 6))

#2

def apply_functions(fs,x):
    for f in fs:
        x = f(x)
    return x
fs = ['...'.join, str.upper,str.lower]
x = "WHAT IS THIS?"
print(apply_functions(fs, x))