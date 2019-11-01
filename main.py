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
eps = 0
num_actions = 4
num_episode = 1000
lr = 0.01
flag_pos = [[4,4]]

action_map = {0:"Up",1:"down",2:"right",3:"left"}
action_map2 = {0:"\u2191",1:"\u2193",2:"\u2192",3:"\u2190"}

grid = gridSim(n,p,flag_pos,"Optimal Action Without Shaping")
pl = player(grid)

Q,stepsPerEpisode=q_learning(pl,lr,eps,num_episode,n*n*len(flag_pos),num_actions,shaping=False)
gui=show_Q_path(n,Q,action_map2,pl,"path without shaping")

grid.__init__(n,p,flag_pos,"Optimal Action With Shaping")
pl.__init__(grid)

Q_shaping,stepsPerEpisode_shaping=q_learning(pl,lr,eps,num_episode,n*n*len(flag_pos),num_actions,shaping=True)
gui=show_Q_path(n,Q_shaping,action_map2,pl,"path with shaping")

gui.mainloop()

plt.scatter(range(num_episode),stepsPerEpisode)
plt.title("Steps/Episode Without Shaping")
plt.show()

plt.scatter(range(num_episode),stepsPerEpisode_shaping)
plt.title("Steps/Episode With Shaping")
plt.show()
