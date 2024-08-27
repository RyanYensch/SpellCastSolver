class App:

  def __init__(self):
    self.board = []
    self.wordList = []
    self.validWordsForBoard = []


    with open("words.txt", 'r') as file:
      for line in file:
        word = line.strip()
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
    pass
  
    





if __name__ == "__main__":
  Game = App()
  Game.fillBoard()
  Game.validWords()
  print(Game.validWordsForBoard)
