lst = list(range(10))

lst = []
for x in range(10):
    lst.append(x**2)

print(lst)

#List comprehension
lst = [f'value {x}' for x in range(10) if x % 3 == 0]

print(lst)