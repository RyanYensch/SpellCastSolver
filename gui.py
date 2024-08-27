import tkinter as tk
from spellCast import App
import threading

class GridWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("5x5 Grid")
        
        self.entries = [[None for _ in range(5)] for _ in range(5)]
        
        for i in range(5):
            for j in range(5):
                self.entries[i][j] = tk.Entry(self.root, width=3)
                self.entries[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=5, column=0, columnspan=5, pady=10)
        
    def calculate(self):
        grid_values = [[entry.get() for entry in row] for row in self.entries]
        
        Game.fillBoardFromWindow(grid_values).validWords

root = tk.Tk()

app = GridWindow(root)
root.mainloop()

if __name__ == '__main__':
  Game = App()
