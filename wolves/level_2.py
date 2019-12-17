def animals_left(days: int):
    wolves = 15681566
    sheeps = 27519230
    snakes = 20773652

    for day in range(1, days):
        sheeps = sheeps - wolves
        snakes = snakes - sheeps
        wolves = wolves - snakes

    return sheeps


counter = 1
while counter:
    counter += 1
    S = animals_left(days=counter)
    if S <= 200:
        print("In the morning of day {}, their is {} sheeps left. K = {}".format(counter, S, counter - 1))
        break
