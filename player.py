from gridSim import *
from gui import *
import numpy as np
# from q_learning import *
import math
class player:
	"""docstring for player"""
	def __init__(self,grid):
		self.grid = grid
		self.initState = 0
		self.states=[[0,0]]
	def transition(self,state,action):
		n = self.grid.n
		# collected = int(state/(n*n))
		x = int((state%(n*n))/n)
		y = state%n
		[x1,y1,collected1,reward,finished]=self.grid.take_action(x,y,action)
		self.states.append([x1,y1])
		next_state=int(collected1*n*n + x1*n + y1)
		if finished:
			next_state-=n*n
		return next_state,reward,finished

	def transition_with_reward_shaping(self,state,action):
		n = self.grid.n
		collected = int(state/(n*n))
		x = int((state%(n*n))/n)
		y = state%n
		[x1,y1,collected1,reward,finished]=self.grid.take_action(x,y,action)
		reward = reward + self.reward_self(x,y,collected,x1,y1)
		self.states.append([x1,y1])
		next_state=int(collected1*n*n + x1*n + y1)
		if finished:
			next_state-=n*n
		return next_state,reward,finished

	def reward_self(self,x,y,collected,x1,y1):
		return self.phi(x,y,collected) - self.phi(x1,y1,collected)

	def phi(self,x,y,collected):
		# return 3
		target = self.grid.flag_pos[collected]
		return abs(x-target[0]) + abs(y-target[1])
		# return math.sqrt((x-target[0])**2 + (y-target[1])**2)

	def reset(self):
		self.states=[[0,0]]
		self.grid.reset()
