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

def q_learning(player,alpha,epsilon,num_episodes,n_states,n_actions,gamma=1,shaping=False):
    Q = [[0]*n_actions for i in range(n_states)]
    stepsPerEpisode=[]
    print("started q_learning")
    for epi in range(num_episodes):
        state = player.initState
        episode_len = 0
        while(1):
            episode_len+=1
            action_probs = EpsilonGreedyPolicy(Q,state,epsilon)
            action = np.random.choice(np.arange(n_actions),p = action_probs)
            if shaping:[next_state,reward,finished]=player.transition_with_reward_shaping(state,action)
            else:[next_state,reward,finished]=player.transition(state,action)
            next_best_action = np.argmax(Q[next_state])
            Q[state][action] = Q[state][action] + alpha*(reward + gamma*Q[next_state][next_best_action]-Q[state][action])
            if(finished):break
            state = next_state
        stepsPerEpisode.append(episode_len)
        # print("length of episode",episode_len)
        if(epi<=num_episodes-2):player.reset()
    return Q,stepsPerEpisode
