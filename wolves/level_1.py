def animals_left(days: int):
    wolves = 322
    sheeps = 567
    snakes = 427

    for day in range(1, days):
        sheeps = sheeps - wolves
        snakes = snakes - sheeps
        wolves = wolves - snakes

    return "Wolves: {}\n" \
           "Sheeps: {}\n" \
           "Snakes: {}".format(wolves, sheeps, snakes)


day_5 = animals_left(5)
print(day_5)
