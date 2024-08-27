
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
        row.append({"letter": line[j], "value": letterValues.get(line[j]), "doubleWord": False})
      self.board.append(row)
    
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
   
  def findWord(self, word):
    rows = columns = 5

    def checker(startingRow, startingColumn, remainingLetters):
      end = False

      if not remainingLetters:
        return True
      if self.board[startingRow][startingColumn]["letter"] != remainingLetters[0]:
        return False

      temp = self.board[startingRow][startingColumn]["letter"]
      self.board[startingRow][startingColumn]["letter"] = "-"

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


      self.board[startingRow][startingColumn]["letter"] = temp

      if end:
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
    for row in range(0, rows):
      for col in range(0, columns):
        if self.board[row][col]["letter"] == word[0]:
          if checker(row, col, word) == True:
            score = calculateScore(values)
            self.foundWords.append({word: score})
            return True

    return False    


  def findAllWords(self):
    for word in self.validWordsForBoard:
      self.findWord(word)



if __name__ == "__main__":
  Game = App()
  Game.fillBoard()
  Game.validWords()
  Game.findAllWords()
  print(Game.foundWords)
