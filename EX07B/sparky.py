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
    under_sparky = "-"
    grid = make_grid(wmap)
    position = find_sparky(wmap)    # position: row, col
    if position == [None, None]:
        return grid
    row = position[0]
    col = position[1]
    for move in moves:
        if move == "N":
            if row - 1 < 0:
                continue
            elif grid[row - 1][col] == "#":
                continue
            else:
                grid[row][col] = under_sparky
                under_sparky = change_state(grid[row - 1][col])
                grid[row - 1][col] = "X"
                row = row - 1
        elif move == "S":
            if row + 1 >= len(grid):
                continue
            elif grid[row + 1][col] == "#":
                continue
            else:
                grid[row][col] = under_sparky
                under_sparky = change_state(grid[row + 1][col])
                grid[row + 1][col] = "X"
                row = row + 1
        elif move == "W":
            if col - 1 < 0:
                continue
            elif grid[row][col - 1] == "#":
                continue
            else:
                grid[row][col] = under_sparky
                under_sparky = change_state(grid[row][col - 1])
                grid[row][col - 1] = "X"
                col = col - 1
        else:
            if col + 1 >= len(grid[0]):
                continue
            elif grid[row][col + 1] == "#":
                continue
            else:
                grid[row][col] = under_sparky
                under_sparky = change_state(grid[row][col + 1])
                grid[row][col + 1] = "X"
                col = col + 1
    for i in range(len(grid)):
        grid[i] = "".join(grid[i])
    return grid


def make_grid(wmap: list):
    """Make a grid with lists within a list."""
    grid = []
    if len(wmap) == 1:
        grid = [list(wmap[0])]
        return grid
    else:
        for i in range(len(wmap)):
            grid.append(list(wmap[i]))
        return grid


def find_sparky(wmap: list):
    grid = make_grid(wmap)
    for i in range(len(grid)):
        for i2 in range(len(grid[i])):
            if grid[i][i2] == "X":
                y = i
                x = i2
            else:
                y = None
                x = None
    return [y, x]


def change_state(new_value):
    if new_value == "W":
        return "w"
    else:
        return "-"
