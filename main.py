from gridSim import *
from gui import * 
import numpy as np 
from q_learning import *


n=5
grid = gridSim(n,0.2)
pl = player(grid)
Q=q_learning(pl,0.01,0.3,100,n*n,4)
action_map = {0:"Up",1:"down",2:"right",3:"left"}
action_map2 = {0:"\u2191",1:"\u2193",2:"\u2192",3:"\u2190"}
gui=App(n,n)
for i in range(len(Q)):
    s=action_map2[np.argmax(Q[i])]
    s2 = action_map[np.argmax(Q[i])]
    print(s2)
    gui.update(i//n,i%n,s[0])
gui.mainloop()
