import random
from gui import *
class gridSim:
	"""docstring for gridSim"""
	
	def __init__(self, n, p,name="hi"):
		# super(gridSim, self).__init__()
		# n x n grid
		# with probability p move in random direction
		self.n = n
		self.p = p
		self.init_pos = [0,0]
		self.grid = [[0]*n for i in range(0,n)]
		self.allowed = [[True]*n for i in range(0,n)]
		self.gui = App(n,n,name)
		self.finish = [n-1,n-1]
		self.finished=False	
	def reset(self):
		# self.gui = App(self.n,self.n)
		self.finished = False
	def take_action(self,i,j,action):
		# action = 0 - Up, 1 - Down, 2 - Right, 3 - Left
		x = random.random()
		reward = -1
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

		if move == 2:
			i1 = i
			if j == self.n-1:
				j1 = j
			else:
				j1 = j+1

		if move == 1:
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

		if(i1==self.finish[0] and j1==self.finish[1]):
			self.finished=True
			# reward=self.n*self.n

		if(self.allowed[i1][j1]):
			return [i1,j1,reward,self.finished] 
		else:
			return [i,j,reward,self.finished]

# if __name__ == "__main__":
#     grid=gridSim(10,0.5)
#     [x,y] = grid.init_pos
#     for i in range(10):
#     	grid.gui.update(x,y,i)
#     	x,y,_=grid.take_action(x,y,2)

#     grid.gui.mainloop()