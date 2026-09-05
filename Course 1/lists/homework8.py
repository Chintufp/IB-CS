#Stage 1
words = []
while (word := input("Enter a word: ")) != "!":
    words.append(word)

#Stage 2
indcies = []
while (index := int(input("Enter an index: "))) != -1:
    indcies.append(index)

results = []
#Stage 3
for i in indcies:
    if i < len(words):
        results.append(words[i])
        #Wallahi don't try to use .pop(), it fucks up the indexing after the first one

print("original: ", words)
print("indcies: ", indcies)
print("results: ", results)
