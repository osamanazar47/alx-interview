#!/usr/bin/python3
"""Module for the island perimeter problem"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    perimeter = 0

    rows = len(grid)
    cols = len(grid[0])

    for j in range(rows):
        for i in range(cols):
            if grid[j][i] == 1:
                # Start with 4 sides
                one_perimeter = 4

                # Check adjacent cells
                if j > 0 and grid[j - 1][i] == 1:  # Up
                    one_perimeter -= 1
                if j < rows - 1 and grid[j + 1][i] == 1:  # Down
                    one_perimeter -= 1
                if i > 0 and grid[j][i - 1] == 1:  # Left
                    one_perimeter -= 1
                if i < cols - 1 and grid[j][i + 1] == 1:  # Right
                    one_perimeter -= 1

                perimeter += one_perimeter

    return perimeter
