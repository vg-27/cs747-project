from gridSim import *
from gui import * 
import numpy as np 
# from q_learning import *

class player:
	"""docstring for player"""
	def __init__(self,grid):
		self.grid = grid
		self.initState = 0

	def transition(self,state,action):
		n = self.grid.n
		x = int(state/n)
		y = state%n;
		[x1,y1,reward,finished]=self.grid.take_action(x,y,action)
		return int(x1*n+y1),reward,finished


	def reset(self):
		self.grid.reset()



