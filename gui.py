import tkinter as tk
from spellCast import App
import threading

x = []

class GridWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("5x5 Grid")
        
        self.entries = [[None for _ in range(5)] for _ in range(5)]
        self.states = [[None for _ in range(5)] for _ in range(5)]

        # Create the grid of Entry widgets
        for i in range(5):
            for j in range(5):
                entry = tk.Entry(self.root, width=3)
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.bind("<Button-3>", lambda e, x=i, y=j: self.show_context_menu(e, x, y))  # Right-click menu
                self.entries[i][j] = entry
        
        # Create the Calculate button
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=5, column=0, columnspan=5, pady=10)

        # Create a context menu
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Set Double Letter", command=lambda: self.set_state("DL", "green"))
        self.context_menu.add_command(label="Set Triple Letter", command=lambda: self.set_state("TL", "yellow"))
        self.context_menu.add_command(label="Set Double Letter", command=lambda: self.set_state("DW", "purple"))
        self.context_menu.add_command(label="Clear", command=lambda: self.set_state(None, "white"))

        # Track the currently selected cell for context menu
        self.current_cell = (0, 0)

    def show_context_menu(self, event, x, y):
        self.current_cell = (x, y)
        self.context_menu.post(event.x_root, event.y_root)

    def set_state(self, state, color):
        x, y = self.current_cell
        self.states[x][y] = state
        self.entries[x][y].config(bg=color)

    def calculate(self):
        grid_values = [[entry.get() for entry in row] for row in self.entries]
        Game.clearData()
        Game.fillBoardFromWindow(grid_values, self.states).validWords()
        def bestWords():
          for swapCount in range(0,4):
            print(swapCount, " swaps: ", Game.getBestWord(swapCount))

        threading.Thread(target=bestWords(0)).start()



if __name__ == '__main__':
  root = tk.Tk()

  Game = App()
  app = GridWindow(root)
  root.mainloop()
  
