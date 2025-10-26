import numpy as np
import os
import time

# === Initial grid ===
grid = np.array([
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
])

def count_alive_neighbors(board, row, col):
    """Count how many alive neighbors a given cell has."""
    alive = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i == row and j == col):
                continue
            alive += board[i, j]
    return alive


def next_generation(grid):
    """Compute the next generation according to the Game of Life rules."""
    
    # Add a border of zeros (padding = 2)
    padded = np.pad(grid, pad_width=2, mode='constant')
    
    # Create a copy for the next state
    new_grid = np.zeros_like(grid)
    
    rows, cols = grid.shape

    # Loop through the playable area (ignore padding)
    for i in range(2, rows + 2):
        for j in range(2, cols + 2):
            neighbors = count_alive_neighbors(padded, i, j)
            cell = padded[i, j]

            # === Apply the rules ===
            if cell == 1 and neighbors in (2, 3):
                new_grid[i - 2, j - 2] = 1
            elif cell == 0 and neighbors == 3:
                new_grid[i - 2, j - 2] = 1
            else:
                new_grid[i - 2, j - 2] = 0

    return new_grid


def display(grid):
    """Pretty print the grid in the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print("".join("█" if cell == 1 else " " for cell in row))
    print()


def run_simulation(grid, delay=0.5):
    """Run the game loop."""
    while True:
        display(grid)
        grid = next_generation(grid)
        time.sleep(delay)


if __name__ == "__main__":
    run_simulation(grid)
