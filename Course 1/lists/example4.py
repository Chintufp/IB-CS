import random
n = 12
lst = random.sample(list(range(n)), n)

print(lst)
out = [b-a for a,b in zip(lst, lst[1:])]
print(out)