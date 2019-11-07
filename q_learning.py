from gridSim import *
from gui import *
from player import *
import numpy as np 

# def EpsilonGreedyPolicy(Q,state,epsilon=0.1):
#     n_actions = len(Q[0])
#     p_a = np.ones(n_actions,dtype=float)*epsilon/n_actions
#     greedyAction = np.argmax(Q[state])
#     p_a[greedyAction]+=(1-epsilon)
#     return p_a

def EpsilonGreedyPolicy(Q,state,epsilon):
    n_actions = len(Q[0])
    if np.random.choice([0,1],p =[epsilon,1-epsilon])==0:
        action = np.random.randint(0,n_actions-1)
    else:
        action = np.argmax(Q[state])
    return action

def estimate_V(Q,n_states,n_actions):
    v = []
    for s in range(n_states):
        best_action = np.argmax(Q[s])
        v.append(Q[s][best_action])
    return v

def q_learning(player,alpha,epsilon,num_episodes,n_states,n_actions,shaping,gamma=1,eps_decay=1.001 ):
    Q = [[0]*n_actions for i in range(n_states)]
    stepsPerEpisode=[]
    print("started q_learning")
    for epi in range(num_episodes):
        state = player.initState
        episode_len = 0
        # if(epi%100 == 0):
        # if shaping==2:
            # v = estimate_V(Q,n_states,n_actions)
        while(1):
            episode_len+=1
            action = EpsilonGreedyPolicy(Q,state,epsilon)
            # action = np.random.choice(np.arange(n_actions),p = action_probs)
            if shaping == 1:
                # [next_state,reward,finished]=player.transition(state,action)
                # reward += v[next_state]-v[state]
                [next_state,reward,finished]=player.transition_with_reward_shaping(state,action,1)
            elif shaping==2:
                [next_state,reward,finished]=player.transition_with_reward_shaping(state,action,2)
            elif shaping == 3:
                v = estimate_V(Q,n_states,n_actions)
                [next_state,reward,finished]=player.transition(state,action)
                reward += v[next_state]-v[state]

            else:
                [next_state,reward,finished]=player.transition(state,action)
            next_best_action = np.argmax(Q[next_state])
            Q[state][action] = Q[state][action] + alpha*(reward + gamma*Q[next_state][next_best_action]-Q[state][action])
            if(finished):break
            state = next_state
            epsilon = epsilon/eps_decay
        stepsPerEpisode.append(episode_len)
        # print("length of episode",episode_len)
        # print(epi)
        if(epi<=num_episodes-2):player.reset()
    return Q,stepsPerEpisode



