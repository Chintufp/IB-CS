flights = ['AY664', 'BA047', 'AF110', 'LH554', 'AY101']
airlines = ['AY', 'UA', 'LH']

print('flights: ', flights)
print('airlines: ', airlines)

for a in airlines:
    print(f'{a}:', end=" ")
    for flight in flights:
        if flight.startswith(a):
            print(flight, end=' ')
    print()