N = 7

k = N
for row in range(N):
    k = N- row
    for number in range(1,k+1):
        print(number, end=" ")
    k -=1
    print()