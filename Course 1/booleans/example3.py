sleep = False

while (day := int(input("Enter a day of the week (1-7): "))) not in range(1, 8):
    print("Please enter a valid day of the week (1-7).")

if day > 5:
    sleep = True
else:
    while (vac := input("Vacation? (y/n): ")) not in ["y", "n"]:
        print("Please enter 'y' or 'n'.")
    if vac == "y":
        sleep = True
    else:
        sleep = False

print(sleep)