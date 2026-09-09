#Stage 1
words = []
while (word := input("Enter a word: ")) != "!":
    words.append(word)

#Stage 2
indcies = []
while (index := int(input("Enter an index: "))) >= 0:
    indcies.append(index)

#Stage 3
results = []
for i in range(len(words)):
    if i not in indcies:
        results.append(words[i])
        # wallahi dont use .pop() cuz it messed up everthing

print("original: ", words)
print("indcies: ", indcies)
print("results: ", results)
