



class Environment:
	"""
	Environment that processes all actions.
	
	:args:
	:map: Map object used to store terrain and car locations
	:config: Config dictionary loaded from a .JSON file
				This stores most relevant variables for movement, etc.

	:methods:
	:step: Moves the environment forward by 1 timestep
	:reset: Resets the environment
	:render: Renders the environment. If the interface is open
			###TODO
	"""
	def __init__(map, config, render_mode=True):
		pass