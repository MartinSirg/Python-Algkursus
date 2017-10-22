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
    for i in range(len(wmap)):  # Finding out where sparky is located
        if "X" in wmap[i]:
            current_position = wmap[i].index("X") + 1 + len(wmap[i])
    positions = {}
    under_sparky = "-"  # First spot under Sparky is always "-"
    for int1 in range(len(wmap)):       # Making the grid with a dictionary(positions)
        current_row = list(wmap[int1])  # Example grid: {"1": "W", "2": "-", "3": "#",
        current_row_number = int1       # \              "4": "w", "5": "w", "6": "X",}
        for int2 in range(len(current_row)):
            positions[len(current_row) * current_row_number + int2 + 1] = current_row[int2]
    for direction in moves:
        if direction == "N":                                            # Sparky goes north!
            if current_position - len(wmap[1]) <= 0:                    # If position is less than 0
                continue                                                # ignore move
            elif positions[current_position - len(wmap[1])] == "#":     # If position above sparky is #
                continue                                                # ignore move
            else:
                if under_sparky == "W":                                 # If Sparky was in tall grass
                    under_sparky = "w"                                  # Memorized value under sparky is short grass(w)
                    positions[current_position] = under_sparky          # Change sparky's last position to Mem. value
                    current_position = current_position - len(wmap[1])  # Change the number of current position
                    under_sparky = positions[current_position]          # Memorize value under new position
                    positions[current_position] = "X"                   # Change the value of the new position to "X"
                else:
                    under_sparky = "-"
                    positions[current_position] = under_sparky
                    current_position = current_position - len(wmap[1])
                    under_sparky = positions[current_position]
                    positions[current_position] = "X"
        elif direction == "S":                                          # Sparky goes south
            if current_position + len(wmap[1]) >= len(positions):       # If new position under sparky is bigger
                continue                                                # than the length of the grid, Ignore move
            elif positions[current_position + len(wmap[1])] == "#":     # If new position under sparky is "#"
                continue                                                # ignore move
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
        elif direction == "E":                                          # Sparky goes east
            if current_position % len(wmap[1]) == 0:                    # If Sparky is on the last position in the row
                continue                                                # ignore move
            elif positions[current_position + 1] == "#":                # if the position to the right of Sparky is "#"
                continue                                                # ignore move
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
        elif direction == "W":                                          # Sparky goes west!
            if current_position % len(wmap[1]) == 1:                    # If sparky is on the first position in the row
                continue                                                # Ignore move
            elif positions[current_position - 1] == "#":                # If the position to the left of Sparky is "#"
                continue                                                # ignore move
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
    temp_list = list(positions.values())
    temp_str = "".join(temp_list)
    final_list = []
    len_of_row = len(wmap[1])
    for i in range(0, len(temp_str), len_of_row):
        final_list.append(temp_str[i:i+len_of_row])
    return final_list
