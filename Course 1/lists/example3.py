lst = ["what", "a", "wondereful", "morning"]

newLst = []
for word in lst:
    if len(word) > 4:
        newLst.append(word)

lst = newLst
print(lst)

# List comphrehension method
lst = ["what", "a", "wondereful", "morning", "nigga"]
lst = [word for word in lst if len(word) > 4]
print(lst)