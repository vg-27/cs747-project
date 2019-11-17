import random
from gui import *
class gridSim:
	"""docstring for gridSim"""

	def __init__(self, n, p, flag_pos, allowed, name="hi"):
		# super(gridSim, self).__init__()
		# n x n grid
		# with probability p move in random direction
		self.n = n
		self.p = p
		self.init_pos = [0,0]
		self.grid = [[0]*n for i in range(0,n)]
		# self.allowed = [[True]*n for i in range(0,n)]
		self.allowed = allowed
		self.gui = App(n,n,name)
		self.flag_pos = flag_pos
		self.collected = 0
		self.finished=False
	def reset(self):
		# self.gui = App(self.n,self.n)
		self.collected = 0
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

		if(i1==self.flag_pos[self.collected][0] and j1==self.flag_pos[self.collected][1]):
			self.collected += 1

		if(self.collected==len(self.flag_pos)):
			self.finished=True
			# reward=self.n*self.n

		if(self.allowed[i1][j1]):
			return [i1,j1,self.collected,reward,self.finished] 
		else:
			return [i,j,self.collected,reward,self.finished]

class htgrid:
	def __init__(self, n,p,allowed,fpos,wpos,name="hi"):
		self.n = n
		self.p = p
		self.allowed = allowed
		self.fpos = fpos
		self.wpos = wpos
		self.gui = App(n,n,name)
		self.finished=False
		self.init_pos = [0,0]


	def reset(self):
		self.finished = False

	def take_action(self,i,j,t,move):
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

		if i1 == self.wpos[0] and j1 == self.wpos[1]:
			t1 = 1
		elif t == 1:
			x = random.random()
			if x < self.p:
				t1 = 0
			else:
				t1 = 1
		else:
			t1 = 0

		if t1 == 1 and i1==self.fpos[0] and j1==self.fpos[1]:
			self.finished = True

		reward = -1
		if self.allowed[i1][j1]:
			return [i1,j1,t1,reward,self.finished] 
		else:
			return [i,j,t1,reward,self.finished]

		

# if __name__ == "__main__":
#     grid=gridSim(10,0.5)
#     [x,y] = grid.init_pos
#     for i in range(10):
#     	grid.gui.update(x,y,i)
#     	x,y,_=grid.take_action(x,y,2)

#     grid.gui.mainloop()
