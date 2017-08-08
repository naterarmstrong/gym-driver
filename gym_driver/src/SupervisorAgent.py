




class Agent:

	def __init__(self, map, search_horizon=4):
		self.map = map
		self.search_horizon = search_horizon
		self.actions = []
		for acc_action in range(3):
			for steer_action in [0, 2, 4]:
				self.actions.append((acc_action, steer_action))

		self.reset()


	def eval_policy(self):
		


	def reset(self):
		self.previous_path = ()
		self.map.reset()
		self.curr_heuristic_cost = 