#primes smaller than 100
primes = []
for x in range(2, 100):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
            break
    if prime:
        primes.append(x)

print(primes)

#
primes = []
x = 2
while len(primes) < 100:
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
            break
    if prime:
        primes.append(x)
    x += 1

print(primes)
print(len(primes))