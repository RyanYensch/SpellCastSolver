# SpellCastSolver
Solves the Spellcast game in discord for the best move


# How To Use
with tklinter and python installed
run the command:
```
python3 gui.py
```

- Fill each tile with the respective letter
- Right Click on any special Tile (Double/Triple Letter, Double Word)
- Select the respective option
- Click calculate and wait for the results to load

## Interpreting swaps
The swaps are labelled in the following format ```(row, column): letter```
This means to swap the letter in the row and column with the letter listed
e.g.
if it was (row: 2, column: 3): a
then you would switch the letter in the second row and the third column with the letter a

## Changing the data
Currently You cannot change the data after pressing calculate while one or more of the results is still being determined
So instead you must close the program and restart it using the command shown earlier


# How To Open From The Binaries
- Download the Spellcast file and words.txt from the latest release
- In your linux terminal type the command ./SpellCast
- If it says you don't have the permissions run the command ```chmod +x SpellCast```
- Then re run the command and the program will run

