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
		self.exp_steps_to_goal=sum([abs(grid.flag_pos[i][0] - grid.flag_pos[i+1][0]) + abs(grid.flag_pos[i][1] - grid.flag_pos[i+1][1]) for i in range(0,len(grid.flag_pos)-1)]) + grid.flag_pos[0][0] + grid.flag_pos[0][1]
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

	def transition_with_reward_shaping(self,state,action,tor):
		n = self.grid.n
		collected = int(state/(n*n))
		x = int((state%(n*n))/n)
		y = state%n
		[x1,y1,collected1,reward,finished]=self.grid.take_action(x,y,action)
		reward = reward + self.reward_self(x,y,collected,x1,y1,collected1,tor)
		self.states.append([x1,y1])
		next_state=int(collected1*n*n + x1*n + y1)
		if finished:
			next_state-=n*n
		return next_state,reward,finished

	def reward_self(self,x,y,collected,x1,y1,collected1,tor):
		if tor==1:
			return self.phi(x,y,collected) - self.phi(x1,y1,collected) 
		elif tor==2:
			return self.phi2(x,y,collected) - self.phi2(x1,y1,collected1) 

	def phi(self,x,y,collected):
		# return 3
		target = self.grid.flag_pos[collected]
		return (abs(x-target[0]) + abs(y-target[1]))
		# return math.sqrt((x-target[0])**2 + (y-target[1])**2)
	def phi2(self,x,y,collected):
		total_flags = len(self.grid.flag_pos)
		# target = self.grid.flag_pos[total_flags-1]
		return (total_flags - collected)*self.exp_steps_to_goal/total_flags
	def reset(self):
		self.states=[[0,0]]
		self.grid.reset()

class htpl:
	"""docstring for htpl"""
	def __init__(self,grid):
		self.grid = grid
		self.initState = 0
		self.states=[[0,0]]
	def transition(self,state,action):
		n = self.grid.n
		# collected = int(state/(n*n))
		t = int(state/(n*n));
		temp = state%(n*n);

		x = int((temp)/n)
		y = temp%n
		[x1,y1,t1,reward,finished]=self.grid.take_action(x,y,t,action)
		self.states.append([x1,y1])
		next_state=int(t1*n*n + x1*n + y1)
		# if finished:
		# 	next_state-=n*n
		return next_state,reward,finished

	def transition_with_reward_shaping(self,state,action,tor):
		n = self.grid.n
		# collected = int(state/(n*n))
		t = int(state/(n*n));
		temp = state%(n*n);

		x = int((temp)/n)
		y = temp%n
		[x1,y1,t1,reward,finished]=self.grid.take_action(x,y,t,action)
		reward = reward + self.reward_self(x,y,t,x1,y1,t1,tor)
		self.states.append([x1,y1])
		next_state=int(t1*n*n + x1*n + y1)
		# if finished:
		# 	next_state-=n*n
		return next_state,reward,finished

	def reward_self(self,x,y,t,x1,y1,t1,tor):
		if tor == 1:
			return self.phi(x,y,t) - self.phi(x1,y1,t1)

	def phi(self,x,y,t):
		distf = abs(self.grid.wpos[0] - self.grid.fpos[0]) + abs(self.grid.wpos[1] - self.grid.fpos[1])
		dist =  abs(self.grid.wpos[0] - x) + abs(self.grid.wpos[1] - y)
		disf =  abs(self.grid.fpos[0] - x) + abs(self.grid.fpos[1] - y)
		p = self.grid.p
		v0 = (1-p)**distf
		ezero = 2*(1-v0)/(p*v0) - distf
		v1 = (1-p)**disf
		egen = 2*(1-v1)/p - (v1)*disf + (ezero + dist)*(1-v1)
		if t == 0:
			# return dist + distf
			if p == 0:
				return dist + distf
			else:
				return dist + ezero
		elif t==1:
	 		# return disf
	 		if p == 0:
	 			return disf
	 		else:
	 			return egen
	 	 	 

	def reset(self):
		self.states=[[0,0]]
		self.grid.reset()