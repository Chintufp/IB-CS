perfectNumbers = []
for i in range(1, 10000):
    sum_of_divisors = 0
    for j in range(1, i):
        if i % j == 0:
            sum_of_divisors += j
    if sum_of_divisors == i:
        perfectNumbers.append(i)

print(perfectNumbers)