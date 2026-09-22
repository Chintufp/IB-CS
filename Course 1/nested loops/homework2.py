# 1. 
# The purpuse is to check if any elements from list a match with list b
# 2. Not very efficient because it contitnues checking even after a duplicate has been found once. (Even though more than one duplicate makes to difference to the output)

#3.
a = [1,2,3,4,5]
b = [5,6,7,8,9]
flag = False
for i in a:
    for j in b:
        if i == j:
            flag = True
            break