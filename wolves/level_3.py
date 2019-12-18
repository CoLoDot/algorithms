def animals_(days):
    wolves = 1
    sheeps = 2
    snakes = 3

    for day in range(1, days):
        wolves = wolves + snakes
        snakes = snakes + sheeps
        sheeps = sheeps + wolves

    return "Wolves: {}\n" \
           "Sheeps: {}\n" \
           "Snakes: {}".format(wolves, sheeps, snakes)


print(animals_(7))
