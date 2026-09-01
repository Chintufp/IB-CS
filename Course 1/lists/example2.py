# lst = []

# while (num:=int(input("Enter a number (less than 0 to stop): "))) >= 0:
#     lst.append(num)
#     lst.sort() # Too much computational work when dealing with large lists

# print(lst)


# Sorting
lst = []

while (num:=int(input("Enter a number (less than 0 to stop): "))) >= 0:
    i = 0
    while i < len(lst) and lst[i] < num:
        i += 1
    lst.insert(i, num)
print(lst)
