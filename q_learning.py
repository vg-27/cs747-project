from gridSim import * 
import numpy as np 
def EpsilonGreedyPolicy(Q,state,epsilon=0.1):
    n_actions = len(Q[0])
    p_a = np.ones(n_actions,dtype=float)*epsilon/n_actions
    greedyAction = np.argmax(Q[state])
    p_a[greedyAction]+=(1-epsilon)
    return p_a

def q_learning(grid,alpha,epsilon,num_episodes,n_states,n_actions,gamma=1):
    Q = [[0]*n_actions for i in range(n_states)]
    n= np.sqrt(n_states)
    for epi in range(num_episodes):
        [x,y]=grid.init_pos
        state = int(x*n + y)
        episode_len = 0
        grid.gui.update(x,y,episode_len)

        while(1):
            episode_len+=1
            action_probs = EpsilonGreedyPolicy(Q,state,epsilon)
            action = np.random.choice(np.arange(n_actions),p = action_probs)
            [x,y,reward,finished]=grid.take_action(x,y,action)
            # if(epi==num_episodes-1):
            grid.gui.update(x,y,episode_len)
            next_state = int(x*n + y)
            next_best_action = np.argmax(Q[next_state])
            Q[state][action] = Q[state][action] + alpha*(reward + gamma*Q[next_state][next_best_action]-Q[state][action])
            if(finished):break
            state = next_state
        print("hi",episode_len)
        # grid.gui.mainloop()
        grid.reset()

    return Q

n=2
grid = gridSim(n,0)
Q=q_learning(grid,0.001,0.1,100,n*n,4)
action_map = {0:"Up",1:"down",2:"right",3:"left"}
for i in range(len(Q)):
    print(action_map[np.argmax(Q[i])])