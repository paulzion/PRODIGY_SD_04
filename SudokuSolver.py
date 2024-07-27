import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

class SudokuSolver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("450x450")

        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j] = ttk.Entry(self, width=3, justify='center', font=('Arial', 18))
                self.cells[i][j].grid(row=i, column=j, padx=5, pady=5, ipadx=5, ipady=5)

        solve_button = ttk.Button(self, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4, pady=10)

        clear_button = ttk.Button(self, text="Clear", command=self.clear_grid)
        clear_button.grid(row=9, column=5, pady=10)

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)

    def solve_sudoku(self):
        grid = self.read_grid()
        if self.backtrack(grid):
            self.display_grid(grid)
        else:
            messagebox.showwarning("Error", "No solution exists for this Sudoku puzzle.")

    def read_grid(self):
        grid = np.zeros((9, 9), dtype=int)
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].get()
                if val.isdigit():
                    grid[i][j] = int(val)
        return grid

    def display_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(grid[i][j]))

    def is_valid(self, grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num or grid[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def find_empty(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i, j
        return None

    def backtrack(self, grid):
        empty = self.find_empty(grid)
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self.is_valid(grid, row, col, num):
                grid[row][col] = num
                if self.backtrack(grid):
                    return True
                grid[row][col] = 0
        return False

if __name__ == "__main__":
    app = SudokuSolver()
    app.mainloop()
