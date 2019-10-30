from gridSim import *
from gui import *
import numpy as np
import math
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

	def transition_with_reward_shaping(self,state,action):
		n = self.grid.n
		x = int(state/n)
		y = state%n;
		[x1,y1,reward,finished]=self.grid.take_action(x,y,action)
		reward = reward + self.reward_self(x,y,x1,y1)
		return int(x1*n+y1),reward,finished

	def reward_self(self,x,y,x1,y1):
		return self.phi(x,y) - self.phi(x1,y1)

	def phi(self,x,y):
		# return 3
		return math.sqrt((x-self.grid.finish[0])**2 + (y-self.grid.finish[1])**2)

	def reset(self):
		self.grid.reset()
