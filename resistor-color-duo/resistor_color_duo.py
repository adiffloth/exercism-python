c = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    return int(str(c.index(colors[0])) + str(c.index(colors[1])))
