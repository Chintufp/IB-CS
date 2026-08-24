def bacteria(t):
	return t * (t - 20) * (t - 100) + 120000


largest_decrease = 0
times = []

for t in range(1, 101):
	decrease = bacteria(t - 1) - bacteria(t)

	if decrease > largest_decrease:
		largest_decrease = decrease
		times = [t]
	elif decrease == largest_decrease:
		times.append(t)

print("Times:", times)

