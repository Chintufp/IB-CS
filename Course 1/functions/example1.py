def abs_value(x):
    return x if x > 0 else -x

# for x in [-5.6,2,-6,0,3]:
#     print(abs_value(x))

def distance(a,b):
    return abs_value(a-b)

print(distance(5,13))