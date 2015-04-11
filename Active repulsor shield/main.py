import random

class ActiveRepulsorShield():


	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.currentPlayer = self.player1
		self.gameboard = [
		['+','x','x','x','x'],
		['x','x','x','x','x'],
		['x','x','x','x','x']
		]

	def __str__(self):
		returnString = "Current player: " + str(self.currentPlayer) + "\n"
		for row in self.gameboard:
			for col in row:
				returnString += col + " "
			returnString += "\n"
		return returnString

	def makeMove(self):
		(i, j) = self.currentPlayer.getMove(self.gameboard)
		for r in range(i, len(self.gameboard)):
			for c in range(j, len(self.gameboard[r])):
				self.gameboard[r][c] = str(self.currentPlayer)
		if self.currentPlayer == self.player1:
			self.currentPlayer = self.player2
		else:
			self.currentPlayer = self.player1
					
	def weHaveAWinner(self):
		return self.gameboard[0][0] != '+'

class AIPlayer():
	def getMove(self, board):
		while True:
			row = random.randint(0,2)
			col = random.randint(0,4)
			print self.getNumberOfMoves(board)
			if board[row][col] == 'x' or board[row][col] == '+':
				if (row,col) == (0,0) and self.getNumberOfMoves(board) > 1:
					continue
				else:
					return (row,col)
	
	def getNumberOfMoves(self, board):
		flat = [item for sublist in board for item in sublist]
		filtered = [item for item in flat, item == 'x' or item == '+']
		return len(filtered)
		
	def __str__(self):
		return "1"
		
class RandomPlayer():
	def getMove(self, board):
		while True:
			row = random.randint(0,2)
			col = random.randint(0,4)
			if board[row][col] == 'x' or board[row][col] == '+':
				return (row,col)
	def __str__(self):
		return "2"
if __name__ == '__main__':
	player1 = AIPlayer()
	player2 = RandomPlayer()
	player1wins = 0
	player2wins = 0	
	
	for n in range(100):
		session = ActiveRepulsorShield(player1, player2)
		while not session.weHaveAWinner():
			session.makeMove()
			print str(session.currentPlayer)
			if session.weHaveAWinner():
				if str(session.currentPlayer) == "1":
					player1wins += 1
				else:
					player2wins += 1
					
	print "Player 1 wins: ",player1wins
	print "Player 2 wins: ",player2wins
