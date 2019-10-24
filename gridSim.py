import random

class gridSim:
	"""docstring for gridSim"""
	
	def __init__(self, n, p):
		# super(gridSim, self).__init__()
		# n x n grid
		# with probability p move in random direction
		self.n = n
		self.p = p
		self.grid = [[0]*n for i in range(0,n)]


	def take_action(self,i,j,action):
		# action = 0 - Up, 1 - Right, 2 - Down, 3 - Right
		x = random.random()
		if x < self.p:
			move = random.randint(0,3)
		else:
			move = action

		if move == 0:
			j1 = j
			if i == 0:
				i1 = i
			else:
				i1 = i-1

		if move == 1:
			i1 = i
			if j == self.n-1:
				j1 = j
			else:
				j1 = j+1

		if move == 2:
			j1 = j
			if i < self.n-1:
				i1 = i + 1
			else:
				i1 = i

		if move == 3:
			i1 = i
			if j > 0:
				j1 = j - 1
			else:
				j1 = j
		#tuple of [row, col, reward]
		return [i1,j1,-1] 
