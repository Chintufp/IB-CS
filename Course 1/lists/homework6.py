import random
n= 10
list_of_lists = [random.sample(list(range(n)), n) for _ in range (5)]

flattened = []
for sublist in list_of_lists:
    for item in sublist:
        flattened.append(item)

print(flattened)

# flattened = [item for sublist in list_of_lists for item in sublist]
# print(flattened)