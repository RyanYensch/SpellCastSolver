import tkinter as tk
from spellCast import App
import threading

class GridWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("5x5 Grid")
        
        self.entries = [[None for _ in range(5)] for _ in range(5)]
        self.states = [[None for _ in range(5)] for _ in range(5)]

        self.create_widgets()
        
        # Initialize a stop event for thread control
        self.stop_event = threading.Event()

    def create_widgets(self):
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
        self.context_menu.add_command(label="Set Double Word", command=lambda: self.set_state("DW", "purple"))
        self.context_menu.add_command(label="Clear", command=lambda: self.set_state(None, "white"))

        # Track the currently selected cell for context menu
        self.current_cell = (0, 0)

        # Labels to display swap results
        self.result_labels = []
        for i, text in enumerate(["No Swaps: ", "One Swap: ", "Two Swaps: ", "Three Swaps: "]):
            label = tk.Label(self.root, text=text + "Calculating...")
            label.grid(row=7 + i, column=0, columnspan=5, sticky='w')
            self.result_labels.append(label)

    def show_context_menu(self, event, x, y):
        self.current_cell = (x, y)
        self.context_menu.post(event.x_root, event.y_root)

    def set_state(self, state, color):
        x, y = self.current_cell
        self.states[x][y] = state
        self.entries[x][y].config(bg=color)

    def calculate(self):
        # Stop any currently running threads
        self.stop_event.set()

        # Clear previous data
        grid_values = [[entry.get() for entry in row] for row in self.entries]
        Game.clearData()
        Game.fillBoardFromWindow(grid_values, self.states).validWords()

        # Create a new stop event for the new thread
        self.stop_event = threading.Event()

        def bestWords():
            for swapCount in range(4):
                if self.stop_event.is_set():
                    print(f"Thread stopped at {swapCount} swaps")
                    break
                
                # Update the label to show "Calculating..." while the result is being fetched
                self.result_labels[swapCount].config(text=self.result_labels[swapCount].cget("text").split(":")[0] + ": Calculating...")

                # Get the best word result
                result = Game.getBestWord(swapCount)
                word = result['word']
                score = result['score']
                swap_info = result['swaps']
                
                # Update the label with the result
                text = f"{swapCount} Swap{'s' if swapCount > 0 else ''}: {word} - {score}"
                if swap_info:
                    text += f" - {create_swap_info_text(swap_info)}"
                self.result_labels[swapCount].config(text=text)
 
        threading.Thread(target=bestWords).start()

        def create_swap_info_text(swaps):
            text = ""
            for (row, col), letter in swaps:
                if text != "":
                    text += " and "
                text += f" (row: {row},col: {col}: {letter})"
            return text


if __name__ == '__main__':
    root = tk.Tk()

    Game = App()
    app = GridWindow(root)
    root.mainloop()
