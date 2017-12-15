from gym.envs.registration import register

register(id='drifty_walk-v0',
         entry_point='gym_drifty_walk.envs:DriftyWalkEnv')
