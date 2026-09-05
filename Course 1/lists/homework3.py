#1
print([x**2 for x in range(8)])

#2 
print([f'2**{x} is {2**x}' for x in range(4)])

#3
print([(a,b) for a,b in enumerate(range(5,11))])