import random, math

r1 = 4
r2 = math.pi
print(r2/r1)

#pt 2



pointsInside = 0
for i in range(10000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        pointsInside += 1

print(pointsInside/10000)


