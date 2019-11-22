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
print(sys.argv)
arguments = sys.argv[1:]
input_file = arguments[0]
num_episode = int(arguments[1])
rs = int(arguments[2])
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

eps = 1
num_actions = 4
lr = 0.5

action_map = {0:"Up",1:"down",2:"right",3:"left"}
action_map2 = {0:"\u2191",1:"\u2193",2:"\u2192",3:"\u2190"}

#################Original Case Without Reward Shaping#########################################
print("Type0")
if problem=='flag':
	grid = gridSim(n,p,flag_pos,allowed,"Optimal Action Without Shaping")
	pl = player(grid)

if problem=="ht":
	grid = htgrid(n,p,allowed,fpos,wpos,"Optimal Action Without Shaping")
	pl = htpl(grid)

res = np.zeros(num_episode) 

for x in range(0,rs):
	np.random.seed(x)
	Q,stepsPerEpisode = q_learning(pl,lr,eps,num_episode,num_states,num_actions,0)
	res = res + np.array(stepsPerEpisode)

res = res/rs
gui=show_Q_path(n,Q,action_map2,pl,"path without shaping")

# plt.plot(range(num_episode),res,label='Without Shaping')
# plt.plot(range(num_episode),np.cumsum(res),label='Without Shaping')

################## Shaping of Type One Of Each Case ###################################
print("Type1")
if problem=="flag":	#manhattan distance from flags
	grid.__init__(n,p,flag_pos,allowed,"Optimal Action With Type1")

if problem=="ht": #expected steps from food
	grid.__init__(n,p,allowed,fpos,wpos,"Optimal Action With Type1")

pl.__init__(grid)

res1 = np.zeros(num_episode)

for x in range(0,rs):
	np.random.seed(x)
	Q_shaping,stepsPerEpisode_shaping = q_learning(pl,lr,eps,num_episode,num_states,num_actions,1)
	res1 = res1 + np.array(stepsPerEpisode_shaping)

res1 = res1/rs
gui=show_Q_path(n,Q_shaping,action_map2,pl,"path with Type1")

# plt.plot(range(num_episode),res1,label='With Shaping')
# plt.plot(range(num_episode),np.cumsum(res1),label='With Shaping')
################## Shaping of Type Two Of Each Case ###################################
print("Type2")
if problem=="flag": #flags collected till now
	grid.__init__(n,p,flag_pos,allowed,"Optimal Action With Shaping 2")
	pl.__init__(grid)
	res2 = np.zeros(num_episode)

	for x in range(0,rs):
		np.random.seed(x)
		Q_shaping,stepsPerEpisode_shaping_2=q_learning(pl,lr,eps,num_episode,num_states,num_actions,2)
		res2 = res2 + np.array(stepsPerEpisode_shaping_2)

	res2 = res2/rs
	gui=show_Q_path(n,Q_shaping,action_map2,pl,"path with shaping 2")

# plt.plot(range(num_episode),stepsPerEpisode_shaping_2,label='With Shaping 2')

################## Shaping of Type three Of Each Case ###################################
print("Type3")
if problem=="flag":	#manhattan distance from flags
	grid.__init__(n,p,flag_pos,allowed,"Optimal Action With Approx V* potential")

if problem=="ht": #expected steps from food
	grid.__init__(n,p,allowed,fpos,wpos,"Optimal Action With Approx V* potential")
pl.__init__(grid)

res3 = np.zeros(num_episode)

for x in range(0,rs):
	np.random.seed(x)
	Q_shaping,stepsPerEpisode_shaping = q_learning(pl,lr,eps,num_episode,num_states,num_actions,3)
	res3 = res3 + np.array(stepsPerEpisode_shaping)

res3 = res3/rs
gui=show_Q_path(n,Q_shaping,action_map2,pl,"path with Type1")

###########Plot1: Where Steps per episodes are shown###############

plt.plot(range(num_episode),res,label='Type0')
plt.plot(range(num_episode),res1,label='Type1')
plt.plot(range(num_episode),res3,label='Type3')

if problem=="flag":
	plt.plot(range(num_episode),res2,label='Type2')
	plt.title("Graph of Flags Problem")

if problem=="ht":
	plt.title("Graph of Hungry-Thirsty")

plt.xlabel("Episodes")
plt.ylabel("Steps Taken")
plt.legend()
if problem=="flag":
	plt.savefig('results/flags/flags_step_per_episode'+str(p)+'.png')

if problem=="ht":
	plt.savefig('results/ht/ht_steps_per_episode'+str(p)+'.png')

plt.show()

#########Plot2: Where Cumulative Steps are shown###############
plt.plot(range(num_episode),np.cumsum(res),label='Type0')
plt.plot(range(num_episode),np.cumsum(res1),label='Type1')
plt.plot(range(num_episode),np.cumsum(res3),label='Type3')

if problem=="flag":
	plt.plot(range(num_episode),np.cumsum(res2),label='Type2')
	plt.title("Graph of Flags Problem")

if problem=="ht":
	plt.title("Graph of Hungry-Thirsty")

plt.xlabel("Episodes")
plt.ylabel("Cumulative Steps Taken")
plt.legend()

if problem=="flag":
	plt.savefig('results/flags/flags_cumulative_steps'+str(p)+'.png')

if problem=="ht":
	plt.savefig('results/ht/ht_cumulative_steps'+str(p)+'.png')

plt.show()