import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class DriftyWalkEnv(gym.Env):
    metadata = {'render.modes':['human'] }
    
    def __init__(self):
    
        # Remarks
        # a) the action_space is a number between -1 and 1. 
        # b) shape = (1,) refers to a number. 
        # c) The action may also be more complicated, e.g. a vector 
        self.action_space = spaces.Box(-1, 1, shape = (1,))
        
        # the walk starts at 0
        self.state = 0
        return None

    def _step(self, action):
    
        reward = 0
        done = False
        
        IntendedStepSize = action
        
        # IntendedStepSize is the step the walker wants to take
        # on average we allow him to achieve that (so it's the average step size)
        
        # ... however we subject the walker to a random influence, the influence of the wind
        #   represented by np.random.normal()
        windInfluence = np.random.normal()
        
        self.state += IntendedStepSize + windInfluence
        
        return np.array(self.state), reward, done, {}
    
    def _reset(self):

        self.state = 0
        print('starting in state:', self.state)
        
        return None
    
    def _render(self, mode='human', close=False):
        
        if close:
            return
        
        print ("current state:", self.state)
        
        return None
