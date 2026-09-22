#1
n = 1
for i in range(6):
    for _ in range(n):
        print('*', end='')
    print((5-i)*'-')
    n+=1
    print()
    
#2
for i in range(6,0,-1):
    for j in range(i):
        print('*' if j%2==0 else '-', end='')
    print()