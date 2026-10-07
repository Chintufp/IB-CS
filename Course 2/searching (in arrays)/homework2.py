students = ['Alissa',' Ben', 'Charlie', 'Dianna']
grades = ['B', 'D', 'B', 'A']

def grade_search(name, grades):
    index = 0
    found = False
    while not found and index < len(grades):
        if students[index] == name:
            found = True
        else:
            index +=1

    if found:
        print(grades[index])
    else: print("Bro ain't your student teach")

grade_search("Charlie", grades)