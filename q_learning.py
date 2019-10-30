from gridSim import *
from gui import * 
from player import *
import numpy as np 
def EpsilonGreedyPolicy(Q,state,epsilon=0.1):
    n_actions = len(Q[0])
    p_a = np.ones(n_actions,dtype=float)*epsilon/n_actions
    greedyAction = np.argmax(Q[state])
    p_a[greedyAction]+=(1-epsilon)
    return p_a

def q_learning(player,alpha,epsilon,num_episodes,n_states,n_actions,gamma=1):
    Q = [[0]*n_actions for i in range(n_states)]
    # n= np.sqrt(n_states)
    for epi in range(num_episodes):
        # [x,y]=grid.init_pos
        # state = int(x*n + y)
        state = player.initState
        episode_len = 0
        # grid.gui.update(x,y,episode_len)
        # print(epi)
        while(1):
            episode_len+=1
            # print("State",state)
            action_probs = EpsilonGreedyPolicy(Q,state,epsilon)
            action = np.random.choice(np.arange(n_actions),p = action_probs)
            # print("Action",action)
            [next_state,reward,finished]=player.transition(state,action)
            # [x,y,reward,finished]=grid.take_action(x,y,action)
            # if(epi==num_episodes-1):
                # grid.gui.update(x,y,episode_len)
            # next_state = int(x*n + y)
            next_best_action = np.argmax(Q[next_state])
            Q[state][action] = Q[state][action] + alpha*(reward + gamma*Q[next_state][next_best_action]-Q[state][action])
            if(finished):break
            state = next_state
        print("length of episode",episode_len)
        player.reset()
    # grid.gui.mainloop()
    return Q

# n=5
# grid = gridSim(n,0.2)
# Q=q_learning(grid,0.01,0.3,1000,n*n,4)
# action_map = {0:"Up",1:"down",2:"right",3:"left"}
# action_map2 = {0:"\u2191",1:"\u2193",2:"\u2192",3:"\u2190"}
# gui=App(n,n)
# for i in range(len(Q)):
#     s=action_map2[np.argmax(Q[i])]
#     s2 = action_map[np.argmax(Q[i])]
#     print(s2)
#     gui.update(i//n,i%n,s[0])
# gui.mainloop()

