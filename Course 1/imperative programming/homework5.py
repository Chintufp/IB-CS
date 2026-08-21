a = int(input("Gimme integer a: "))
b = int(input("Gimme integer b: "))

# 1
output = None
if a >= 100 and b <= 100:
    output = 1
else:
    output = 0

#2

if (a >= 100 and b <= 50) or (b >= 100 and a <= 50):
    output = 1
else:
    output = 0

print(output)
