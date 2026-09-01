firstStage = []

print("STAGE 1")
while (word := input("Enter a word (type '!' to stop): ")) != "!":
    firstStage.append(word)

print("STAGE 2")
while (word := input("Enter a word (type '!' to stop): ")) != "!":
    if word in firstStage:
        print("hit")
    
