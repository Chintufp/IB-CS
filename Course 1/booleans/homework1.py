sunscreen = False

while (sunny := input("Is it sunny today? (y/n): ")) not in ["y", "n"]:
    print("Please enter 'y' or 'n'.")

if sunny == "y":
    while (time := int(input("What time is it? (0-23): "))) not in range(0, 24):
        print("Please enter a valid time (0-23).")
    if 10 <= time <= 16:
        sunscreen = True
    else:
        sunscreen = False

print("Please use sunscreen")