from gridSim import *
from gui import *
import numpy as np
from q_learning import *
import matplotlib.pyplot as plt
def show_Q_path(n,Q,action_map2,pl,name):
	gui0=App(n,n,name)
	for i in range(n*n):
	    s=action_map2[np.argmax(Q[i])]
	    # s2 = action_map[np.argmax(Q[i])]
	    gui0.update(int((i%(n*n))/n),i%n,s[0])
	for j in range(len(pl.states)):
		pl.grid.gui.update(pl.states[j][0],pl.states[j][1],j)
	return gui0
n=5
p=0
eps = 1
num_actions = 4
num_episode = 250
lr = 0.5
flag_pos = [[1,4],[2,0],[3,4],[4,0]]
# flag_pos = [[0,4],[2,2]]

num_states = n*n*len(flag_pos)


action_map = {0:"Up",1:"down",2:"right",3:"left"}
action_map2 = {0:"\u2191",1:"\u2193",2:"\u2192",3:"\u2190"}

grid = gridSim(n,p,flag_pos,"Optimal Action Withounum_actionst Shaping")

pl = player(grid)
Q,stepsPerEpisode=q_learning(pl,lr,eps,num_episode,num_states,num_actions,0)
print(estimate_V(Q,num_states,num_actions))
gui=show_Q_path(n,Q,action_map2,pl,"path without shaping")

grid.__init__(n,p,flag_pos,"Optimal Action With Shaping")
pl.__init__(grid)

Q_shaping,stepsPerEpisode_shaping=q_learning(pl,lr,eps,num_episode,num_states,num_actions,1)
print(estimate_V(Q_shaping,num_states,num_actions))
gui=show_Q_path(n,Q_shaping,action_map2,pl,"path with shaping")

grid.__init__(n,p,flag_pos,"Optimal Action With Shaping 2")
pl.__init__(grid)

Q_shaping,stepsPerEpisode_shaping_2=q_learning(pl,lr,eps,num_episode,num_states,num_actions,2)
print(estimate_V(Q_shaping,num_states,num_actions))
gui=show_Q_path(n,Q_shaping,action_map2,pl,"path with shaping 2")

# gui.mainloop()

# plt.scatter(range(num_episode),stepsPerEpisode)
plt.plot(range(num_episode),stepsPerEpisode,label='Without Shaping')
plt.xlabel("Episodes")
plt.ylabel("Steps Taken")

# plt.title("Steps/Episode Without Shaping")
# plt.show()

# plt.scatter(range(num_episode),stepsPerEpisode_shaping)
plt.plot(range(num_episode),stepsPerEpisode_shaping,label='With Shaping')
plt.plot(range(num_episode),stepsPerEpisode_shaping_2,label='With Shaping 2')
plt.title("Graph of Flag Grid")
plt.legend()
plt.savefig('flag_grid_2.png')
plt.show()
