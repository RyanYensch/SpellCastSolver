class App:
  
  def __init__(self):
    self.board = []
    self.wordList = []

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

   

  
    





if __name__ == "__main__":
  Game = App()
  Game.fillBoard()