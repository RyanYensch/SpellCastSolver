import threading



letterValues = {
    "a": 1,
    "b": 4,
    "c": 5,
    "d": 3,
    "e": 1,
    "f": 5,
    "g": 3,
    "h": 4,
    "i": 1,
    "j": 7,
    "k": 3,
    "l": 3,
    "m": 4,
    "n": 2,
    "o": 1,
    "p": 4,
    "q": 8,
    "r": 2,
    "s": 2,
    "t": 2,
    "u": 4,
    "v": 5,
    "w": 5,
    "x": 7,
    "y": 4,
    "z": 8,
}

class App:

  def __init__(self):
    self.board = []
    self.wordList = []
    self.validWordsForBoard = []
    self.foundWords = []
    self.letterValues = letterValues


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
        row.append({"letter": line[j], "value": self.letterValues.get(line[j]), "doubleWord": False})
      self.board.append(row)
    
    print("Special Letters (No Spaces):")
    print("Row, Column (1-5), e.g. (14 for row 1 column 4)")
    doubleLetter = input("Double Letter Coords (Row Column) (Enter To Skip): ")
    if doubleLetter:
      DLrow = int(doubleLetter[0]) - 1
      DLcol = int(doubleLetter[1]) - 1
      self.board[DLrow][DLcol]["value"] = self.board[DLrow][DLcol]["value"] * 2

    tripleLetter = input("Triple Letter Coords (Row Column) (Enter To Skip): ")
    if tripleLetter:
      TLrow = int(tripleLetter[0]) - 1
      TLcol = int(tripleLetter[1]) - 1
      self.board[TLrow][TLcol]["value"] = self.board[TLrow][TLcol]["value"] * 3

    doubleWord = input("Double Word Coords (Row Column) (Enter To Skip): ")
    if doubleWord:
      DWrow = int(doubleWord[0]) - 1
      DWcol = int(doubleWord[1]) - 1
      self.board[DWrow][DWcol]["doubleWord"] = True

    return self
  
  def fillBoardFromWindow(self, grid, gridStates):
    for gridRow in grid:
      row = []
      for col in gridRow:
         row.append({"letter": col, "value": self.letterValues.get(col), "doubleWord": False})
      self.board.append(row)

    for stateRow in range(len(gridStates)):
      for col in range(len(gridStates[stateRow])):
        state = gridStates[stateRow][col]
        if state == 'DW':
          self.board[stateRow][col]["doubleWord"] = True
        elif state == 'DL':
          self.board[stateRow][col]['value'] *= 2
        elif state == 'TL':
          self.board[stateRow][col]['value'] *= 3

    return self

  def validWords(self):
    boardLetters = set()
    for row in self.board:
      for letter in row:
        boardLetters.add(letter["letter"])

    for word in self.wordList:
      for letter in word:
        if letter not in boardLetters:
          break
      else:
        self.validWordsForBoard.append(word)
    return self
   
  def findWord(self, word, swaps):
    rows = columns = 5

    def checker(startingRow, startingColumn, remainingLetters, swaps):
      end = False
      swapHappened = False

      if not remainingLetters:
        return True
      if self.board[startingRow][startingColumn]["letter"] != remainingLetters[0]:
        if swaps != 0 and self.board[startingRow][startingColumn]["letter"] != '-':
          swapHappened = True
          swapDone = ((startingRow + 1, startingColumn + 1), remainingLetters[0])
          swaps -= 1
        else:     
          return False

      temp = self.board[startingRow][startingColumn]["letter"]
      self.board[startingRow][startingColumn]["letter"] = "-"

      if startingRow > 0 and startingColumn > 0:
        end = end or checker(startingRow - 1, startingColumn - 1, remainingLetters[1:], swaps)
      if startingRow > 0:
        end = end or checker(startingRow - 1, startingColumn, remainingLetters[1:], swaps)
      if startingRow > 0 and startingColumn < 4:
        end = end or checker(startingRow - 1, startingColumn + 1, remainingLetters[1:], swaps)
      if startingColumn > 0:
        end = end or checker(startingRow, startingColumn - 1, remainingLetters[1:], swaps)
      if startingColumn < 4:
        end = end or checker(startingRow, startingColumn + 1, remainingLetters[1:], swaps)
      if startingRow < 4 and startingColumn > 0:
        end = end or checker(startingRow + 1, startingColumn - 1, remainingLetters[1:], swaps)
      if startingRow < 4:
        end = end or checker(startingRow + 1, startingColumn, remainingLetters[1:], swaps)
      if startingRow < 4 and startingColumn < 4:
        end = end or checker(startingRow + 1, startingColumn + 1, remainingLetters[1:], swaps)


      self.board[startingRow][startingColumn]["letter"] = temp

      if end:

        if swapHappened == True:
          swapValue = self.board[startingRow][startingColumn]["value"]
          swapValue = swapValue / self.letterValues.get(self.board[startingRow][startingColumn]["letter"]) * self.letterValues.get(remainingLetters[0])
          swapsMade.append(swapDone)
        else:
          values.append(self.board[startingRow][startingColumn])  

      return end
    

    def calculateScore(values):
      score = 0
      doubleWord = False
      for letter in values:
        score += letter["value"]
        if letter["doubleWord"] == True:
          doubleWord = True
      
      if doubleWord == True:
        score = score * 2
      
      if len(values) >= 6:
        score += 10

      return score

      

    values = []
    swapsMade = []
    for row in range(0, rows):
      for col in range(0, columns):
        if self.board[row][col]["letter"] == word[0]:
          if checker(row, col, word, swaps) == True:
            score = calculateScore(values)
            self.foundWords.append({"word": word, "score":score, "swaps": swapsMade})
            return True

    return False    


  def findAllWords(self, swaps):
    if swaps == 0:
      for word in self.validWordsForBoard:
        self.findWord(word, swaps)
    else:
      for word in self.wordList:
        self.findWord(word, swaps)
    
    get_score = lambda x: x['score']
    self.foundWords.sort(key=get_score, reverse=True)

    
  def getBestWord(self, swaps):
    self.findAllWords(swaps)
    if len(self.foundWords) != 0:
      return self.foundWords[0]
    else:
      return []
  
  def clearData(self):
    self.board = []
    self.foundWords = []
    self.validWordsForBoard = []


if __name__ == "__main__":
  Game = App()
  Game.fillBoard().validWords()
  def bestWords(swapCount):
    print(swapCount, " swaps: ", Game.getBestWord(swapCount))
  
  for i in range(0,3+1):
    threading.Thread(target=bestWords(i)).start()