cards = int(input("What da value of yo cards?: "))

action = None

if cards < 17:
    action = "HIT"
elif cards > 21:
    action = "BUST"
else:
    action = "STAND"

print(action)