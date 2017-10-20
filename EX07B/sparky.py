"""Simulation."""


def simulate(wmap: list, moves: list) -> list:
    """
    Simulate a robotic lawn mower.

    :param wmap: A list of strings indicating rows that make up the map.
                 The map is always rectangular and the minimum given size is 1x1.
                 Cut grass is indicated by the symbol ('-'), low grass by ('w') and high grass by ('W').
                 The robot position is indicated by the symbol ('X'). There is always one robot on the map.
                 Obstacles are indicated by the symbol ('#').

    :param moves: A list of moves.
                  The moves are abbreviated N - north, E - east, S - south, W - west.
                  Ignore moves that would put the robot out of bounds or crash it into an obstacle.

    :return: A list of strings indicating rows that make up the map. Same format as the given wmap.

    Grass under Sparky's starting position is always cut grass ('-').
    If Sparky mows high grass, it first turns into low grass ('w') and then from low grass into cut grass ('-').
    """
    current_position = 1
    for i in range(len(wmap)):
        if "X" in wmap[i]:
            current_position = wmap[i].index("X") + 1 + len(wmap[i])
    positions = {}
    under_sparky = "-"
    for int1 in range(len(wmap)):
        current_row = list(wmap[int1])
        current_row_number = int1
        for int2 in range(len(current_row)):
            positions[len(current_row) * current_row_number + int2 + 1] = current_row[int2]
    for direction in moves:
        if direction == "N":
            if positions[current_position - len(wmap[1])] == "#":
                continue
            elif current_position - len(wmap[1]) <= 0:
                continue
            else:
                if under_sparky == "W":
                    under_sparky = "w"
                    positions[current_position] = under_sparky
                    current_position = current_position - len(wmap[1])
                    under_sparky = positions[current_position]
                    positions[current_position] = "X"
                else:
                    under_sparky = "-"
                    positions[current_position] = under_sparky
                    current_position = current_position - len(wmap[1])
                    under_sparky = positions[current_position]
                    positions[current_position] = "X"
        elif direction == "S":
            if positions[current_position + len(wmap[1])] == "#":
                continue
            elif current_position + len(wmap[1]) >= len(positions):
                continue
            else:
                if under_sparky == "W":
                    under_sparky = "w"
                    positions[current_position] = under_sparky
                    current_position = current_position + len(wmap[1])
                    under_sparky = positions[current_position]
                    positions[current_position] = "X"
                else:
                    under_sparky = "-"
                    positions[current_position] = under_sparky
                    current_position = current_position + len(wmap[1])
                    under_sparky = positions[current_position]
                    positions[current_position] = "X"
        elif direction == "E":
            if positions[current_position + 1] == "#":
                continue
            elif current_position + 1 >= #x rea max pikkus:
                continue
            else:
                if under_sparky == "W":
                    under_sparky = "w"
                    positions[current_position] = under_sparky
                    current_position = current_position + 1
                    under_sparky = positions[current_position]
                    positions[current_position] = "X"
                else:
                    under_sparky = "-"
                    positions[current_position] = under_sparky
                    current_position = current_position + 1
                    under_sparky = positions[current_position]
                    positions[current_position] = "X"
        elif direction == "W":
            if positions[current_position - 1 ] == "#":
                continue
            elif current_position -1 1 >= #x rea min pikkus:
                continue
            else:
                if under_sparky == "W":
                    under_sparky = "w"
                    positions[current_position] = under_sparky
                    current_position = current_position - 1
                    under_sparky = positions[current_position]
                    positions[current_position] = "X"
                else:
                    under_sparky = "-"
                    positions[current_position] = under_sparky
                    current_position = current_position - 1
                    under_sparky = positions[current_position]
                    positions[current_position] = "X"
    return positions





wmap1 = [
        "#Www-",
        "wXw#-",
    ]

moves1 = ["N", "E", "E", "S", "E"]

print(simulate(wmap1,moves1))