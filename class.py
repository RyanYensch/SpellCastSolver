class App:

  def __init__(self):
    self.board = []
    self.wordList = []
    self.validWordsForBoard = []
    self.foundWords = []


    with open("words.txt", 'r') as file:
      for line in file:
        word = line.strip()
        if len(word) > 1:
          self.wordList.append(word)

  def fillBoard(self):
    self.board.clear()

    print("Enter Board")
    for i in range (0, 5):
      line = input("Line {}: ".format(i+1))
      row = []
      for j in range(0,5):
        row.append(line[j])
      self.board.append(row)
    
    return self
  
  def validWords(self):
    boardLetters = set()
    for row in self.board:
      for letter in row:
        boardLetters.add(letter)

    for word in self.wordList:
      for letter in word:
        if letter not in boardLetters:
          break
      else:
        self.validWordsForBoard.append(word)
    return self
   
  def findWord(self, word):
    rows = columns = 5

    def checker(startingRow, startingColumn, remainingLetters):
      end = False
      

      if not remainingLetters:
        return True
      if self.board[startingRow][startingColumn] != remainingLetters[0]:
        return False

      temp = self.board[startingRow][startingColumn]
      self.board[startingRow][startingColumn] = "-"

      if startingRow > 0 and startingColumn > 0:
        end = end or checker(startingRow - 1, startingColumn - 1, remainingLetters[1:])
      if startingRow > 0:
        end = end or checker(startingRow - 1, startingColumn, remainingLetters[1:])
      if startingRow > 0 and startingColumn < 4:
        end = end or checker(startingRow - 1, startingColumn + 1, remainingLetters[1:])
      if startingColumn > 0:
        end = end or checker(startingRow, startingColumn - 1, remainingLetters[1:])
      if startingColumn < 4:
        end = end or checker(startingRow, startingColumn + 1, remainingLetters[1:])
      if startingRow < 4 and startingColumn > 0:
        end = end or checker(startingRow + 1, startingColumn - 1, remainingLetters[1:])
      if startingRow < 4:
        end = end or checker(startingRow + 1, startingColumn, remainingLetters[1:])
      if startingRow < 4 and startingColumn < 4:
        end = end or checker(startingRow + 1, startingColumn + 1, remainingLetters[1:])


      self.board[startingRow][startingColumn] = temp
      return end

    for row in range(0, rows):
      for col in range(0, columns):
        if self.board[row][col] == word[0]:
          if checker(row, col, word) == True:
            self.foundWords.append(word)
            return True

    return False    


  def findAllWords(self):
    for word in self.wordList:
      self.findWord(word)
    
    print(self.foundWords)




if __name__ == "__main__":
  Game = App()
  Game.fillBoard()
  Game.validWords()
  Game.findAllWords()
