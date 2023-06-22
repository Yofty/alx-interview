#/usr/bin/python3
'''0-island_perimeter.py'''


def island_perimeter(grid):
    '''return the perimetes of the islan'''
    counter = 0
    grid_m = len(grid) - 1
    lst_m = len(grid[0]) - 1

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                if land_idx == 0:
                    counter += 1

                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_m:
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    counter += 1
                else:
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    if lst[land_idx + 1] == 0:
                        counter += 1

                if lst_idx == 0:
                    counter += 1

                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

                elif lst_idx == grid_m:
                    if grid[lst_idx -1][land_idx] == 0:
                        counter += 1

                    counter += 1

                else:
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    if grid[lst_idx +1][land_idx] == 0:
                        counter += 1

    return counter
