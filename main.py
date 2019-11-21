from gridSim import *
from gui import *
import numpy as np
from q_learning import *
import matplotlib.pyplot as plt
import sys

def show_Q_path(n,Q,action_map2,pl,name):
	gui0=App(n,n,name)
	for i in range(n*n):
	    s=action_map2[np.argmax(Q[i])]
	    # s2 = action_map[np.argmax(Q[i])]
	    gui0.update(int((i%(n*n))/n),i%n,s[0])
	for j in range(len(pl.states)):
		pl.grid.gui.update(pl.states[j][0],pl.states[j][1],j)
	return gui0

arguments = sys.argv[1:]

input_file = arguments[0]
num_episode = int(arguments[1])
nit = int(arguments[2])
problem = arguments[3]

inp_file_obj = open(input_file,	"r")
n = int(inp_file_obj.readline())
p = float(inp_file_obj.readline())

allowed = [[True]*n for i in range(0,n)]
for i in range(0,n):
	j = 0
	for val in inp_file_obj.readline().split():
		if int(val) == 0:
			allowed[i][j] = False
		j = j + 1

if problem=="ht":
	fpos = [int(x) for x in inp_file_obj.readline().split()]
	wpos = [int(x) for x in inp_file_obj.readline().split()]
	num_states = n*n*2


if problem=="flag":
	num_flags = int(inp_file_obj.readline())
	num_states = n*n*num_flags
	flag_pos = []
	for i in range(0,num_flags):
		flag_pos.append([int(x) for x in inp_file_obj.readline().split()])


# nit = 1
# n=10
# p=0.1
# num_episode = 1000


eps = 1
num_actions = 4
lr = 0.5

#######Flag positions############
# flag_pos = [[1,4],[2,0],[3,4],[4,0]]
# flag_pos = [[0,4],[2,2]]
# flag_pos = [[6,1]]
# flag_pos = [[0,9],[8,0],[5,4],[3,9],[6,0],[9,9]]


# allowed[0][1] = False
# allowed[1][0:8] = [False]*8
# allowed[3][1:10] = [False]*9
# allowed[5][0:5] = [False]*5
# allowed[5][6:10] = [False]*4
# allowed[7][2:8] = [False]*6
# allowed[6][2] = False

##water and food positions###
# fpos = [9,9]
# wpos = [0,9]

# num_states = n*n*len(flag_pos)
# num_states = n*n*2


action_map = {0:"Up",1:"down",2:"right",3:"left"}
action_map2 = {0:"\u2191",1:"\u2193",2:"\u2192",3:"\u2190"}

#################Original Case Without Reward Shaping#########################################

if problem=='flag':
	grid = gridSim(n,p,flag_pos,allowed,"Optimal Action Withounum_actionst Shaping")
	pl = player(grid)

if problem=="ht":
	grid = htgrid(n,p,allowed,fpos,wpos,"Optimal Action Without Shaping")
	pl = htpl(grid)

res = np.zeros(num_episode)

for x in range(0,nit):
	Q,stepsPerEpisode = q_learning(pl,lr,eps,num_episode,num_states,num_actions,0)
	res = res + np.array(stepsPerEpisode)

res = res/nit

print(estimate_V(Q,num_states,num_actions))
gui=show_Q_path(n,Q,action_map2,pl,"path without shaping")

# plt.plot(range(num_episode),res,label='Without Shaping')
# plt.plot(range(num_episode),np.cumsum(res),label='Without Shaping')

################## Shaping of Type One Of Each Case ###################################

# grid.__init__(n,p,flag_pos,allowed,"Optimal Action With Shaping")
if problem=="flag":	
	grid.__init__(n,p,flag_pos,allowed,"Optimal Action With Shaping")

if problem=="ht":
	grid.__init__(n,p,allowed,fpos,wpos,"Optimal Action With Shaping")

pl.__init__(grid)

res1 = np.zeros(num_episode)

for x in range(0,nit):
	Q_shaping,stepsPerEpisode_shaping = q_learning(pl,lr,eps,num_episode,num_states,num_actions,1)
	res1 = res1 + np.array(stepsPerEpisode_shaping)

res1 = res1/nit

print(estimate_V(Q_shaping,num_states,num_actions))
gui=show_Q_path(n,Q_shaping,action_map2,pl,"path with shaping")

# plt.plot(range(num_episode),res1,label='With Shaping')
# plt.plot(range(num_episode),np.cumsum(res1),label='With Shaping')
#############################################################################################

if problem=="flag":
	grid.__init__(n,p,flag_pos,allowed,"Optimal Action With Shaping 2")
	
	pl.__init__(grid)

	res2 = np.zeros(num_episode)

	for x in range(0,nit):
		Q_shaping,stepsPerEpisode_shaping_2=q_learning(pl,lr,eps,num_episode,num_states,num_actions,2)
		res2 = res2 + np.array(stepsPerEpisode_shaping_2)

	res2 = res2/nit

	print(estimate_V(Q_shaping,num_states,num_actions))
	gui=show_Q_path(n,Q_shaping,action_map2,pl,"path with shaping 2")

# plt.plot(range(num_episode),stepsPerEpisode_shaping_2,label='With Shaping 2')

##############################################################################################



# grid.__init__(n,p,flag_pos,allowed,"Optimal Action With Approx V* potential")
# grid.__init__(n,p,allowed,fpos,wpos,"Optimal Action With Approx V* potential")

# pl.__init__(grid)

# Q_shaping,stepsPerEpisode_shaping_2=q_learning(pl,lr,eps,num_episode,num_states,num_actions,3)
# print(estimate_V(Q_shaping,num_states,num_actions))
# gui=show_Q_path(n,Q_shaping,action_map2,pl,"path with Approx V* potential")

# plt.plot(range(num_episode),stepsPerEpisode_shaping_2,label='With Approx V* potential')

##############################################################################################

# gui.mainloop()

# plt.scatter(range(num_episode),stepsPerEpisode)


# plt.title("Steps/Episode Without Shaping")
# plt.show()

# plt.scatter(range(num_episode),stepsPerEpisode_shaping)

###########Plot1: Where Steps per episodes are shown###############

plt.plot(range(num_episode),res,label='Without Shaping')
plt.plot(range(num_episode),res1,label='With Shaping of Type1')

if problem=="flag":
	plt.plot(range(num_episode),res2,label='With Shaping of Type2')
	plt.title("Graph of Flags Problem")

if problem=="ht":
	plt.title("Graph of Hungry-Thirsty")

plt.xlabel("Episodes")
plt.ylabel("Steps Taken")
plt.legend()
if problem=="flag":
	plt.savefig('flags_step_per_episode.png')

if problem=="ht":
	plt.savefig('ht_steps_per_episode.png')

plt.show()

#########Plot1: Where Cumulative Steps are shown###############
plt.plot(range(num_episode),np.cumsum(res),label='Without Shaping')
plt.plot(range(num_episode),np.cumsum(res1),label='With Shaping of Type1')

if problem=="flag":
	plt.plot(range(num_episode),np.cumsum(res2),label='With Shaping of Type2')
	plt.title("Graph of Flags Problem")

if problem=="ht":
	plt.title("Graph of Hungry-Thirsty")

plt.xlabel("Episodes")
plt.ylabel("Cumulative Steps Taken")
plt.legend()

if problem=="flag":
	plt.savefig('flags_cumulative_steps.png')

if problem=="ht":
	plt.savefig('ht_cumulative_steps.png')

plt.show()