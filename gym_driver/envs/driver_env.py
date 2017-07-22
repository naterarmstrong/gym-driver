import gym
from gym import error, spaces, utils
from gym.utils import seeding

class DriverEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
  	pass
  	self.env = gateway.entry_point # Gets an instance of the environment
  	# Something or other initializing the java code then creating the gateway, and setting gateway to it

  def _step(self, action):
  	return self.env.step(action) # Assuming that this returns the observation tuple

  def _reset(self):
  	self.env.reset()

  def _render(self, mode='human', close=False):
  	self.env.render(mode, close)