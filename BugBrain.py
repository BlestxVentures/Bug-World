
import logging
import neat as NEAT
import numpy as np

'''
This encapsulates the functionality of a bug brain.  Everything is at the individual genome level

- be able to display itself
- should have bias neurons
- can have periodic neurons to invoke time/dependent behavior

BugBrainInterface -- a bug must implement this interface to have a brain
	- has a genome
	- brain is created from genome
	- has inputs and outputs from the brain
	- must normalize its own inputs
	- must support an activation method so can take inputs and provide outputs

- Must be able to create a new bug from a genome.

- Must be able to save itself to a file and save the file name
- Must be able to load itself from a file to create
- Must hide what type of network is being used(e.g., FF, RNN, CTRNN)
'''


class BugBrainInterface:

	def __init__(self, owner, config, genome):
		self._owner = owner

		# assume that the inputs are set before activate
		self._brain_data = {}

		if genome:
			#create a brain with a genome
			self.create_brain(config, genome)
		else:
			#TODO: use the config to create a genome
			#TODO: create a brain with a genome
			logging.error("No genome detected for bug: " + self.owner.name )

	def create_brain(self, config, genome):
		# create a new brain

		self.net = NEAT.nn.feed_forward.FeedForwardNetwork.create(genome, config)

	def activate(self):
		# normalize inputs
		# activate the neural net
		# update state if outputs are to be used as inputs
		# return outputs

		# get the inputs to the net from the sensors
		inputs = self.get_scaled_state()
	
		# run the inputs the nets activation collect the outputs (i.e., action)
		action = self.net.activate(inputs)

		'''
		Outputs Phase 1
	
		- right_wheel_velocity
		- left_wheel_velocity
		'''
		return action

	def update_brain_inputs(self, brain_data):
		"""brain_data: dictionary of key value pairs. keys used:
			right_eye = color=tuple(R,G,B), dist_sqrd, dx, dy
			left_eye = color=tuple(R,G,B), dist_sqrd, dx, dy
				dist_sqrd = distance that the eye detected the colors provided
				dx = the x distance between center of bug and detected object
				dy = the x distance between center of bug and detected object
				(associated with the colors passed at same call)
			vel_r = the velocity of the right wheel from the last time step
			vel_l = the velocity of the right wheel from the last time step

		"""
		# update the local copy with any data passed in.
		# TODO: this is redundant and ugly error-prone code.  fix it
		# for the eyes, cache the closest object to center of eye hit box TODO:make this closest to the bug
		if 'right_eye' in brain_data:  # see if we are working with the right eye data
			if 'right_eye' in self._brain_data:  # see if there is already some data cached
				curr_data = self._brain_data.get('right_eye')  # get cached data
				new_data = brain_data.get('right_eye')  # get the potential update

				# if the potential object is closer, use it, otherwise leave it alone
				if new_data.get('dist_sqrd') < curr_data.get('dist_sqrd'):
					self._brain_data.update(brain_data)
				return
			else:
				self._brain_data.update(brain_data)
				return

		if 'left_eye' in brain_data:  # see if we are working with the left eye data
			if 'left_eye' in self._brain_data:  # see if there is already some data cached
				curr_data = self._brain_data.get('left_eye')  # get cached data
				new_data = brain_data.get('left_eye')  # get the potential update

				# if the potential object is closer, use it, otherwise leave it alone
				if new_data.get('dist_sqrd') < curr_data.get('dist_sqrd'):
					self._brain_data.update(brain_data) # only update the brain if it was closer
				return
			else:  # if no cached data, just store it
				self._brain_data.update(brain_data)
				return

		self._brain_data.update(brain_data)  # if not dealing with the eyes, just update the data

	def scale_to_zero_to_one(self, x):
		# sigmoid goes from [0,1]
		value = 1.0 / (1.0 + np.exp(-x))
		return value

	def scale_to_neg_one_to_one(self, x):
		# tanh goes from [-1,1]
		return np.tanh(x)

	def cap_zero_to_one(self, x):
		if x < 0:
			return 0.0
		elif x > 1:
			return 1.0
		else:
			return x

	def get_scaled_state(self):

		# must match num_inputs from config file
		# should scale from -1 to 1 or 0 to 1 to help the neural net stabilize and converge
		inputs = []

		# get the data from what the right eye saw if anything, otherwise return empty dict
		curr_data = self._brain_data.get("right_eye", {})
		(r, g, b) = curr_data.get("color", (0, 0, 0))
		dx = curr_data.get('dx', 0)
		dy = curr_data.get('dy', 0)

		inputs.append(r/100.0)
		inputs.append(g/100.0)
		inputs.append(b/100.0)
		inputs.append(dx)
		inputs.append(dy)

		# get the data from what the left eye saw if anything, otherwise return empty dict
		curr_data = self._brain_data.get("left_eye", {})
		(r, g, b) = curr_data.get("color", (0, 0, 0))
		dx = curr_data.get('dx', 0)
		dy = curr_data.get('dy', 0)
		inputs.append(r/100.0)
		inputs.append(g/100.0)
		inputs.append(b/100.0)

		# TODO: fix this hard coding of max dist
		# normalize so numbers stay between 0 and 1
		max_dist = 61  # bug_radius + 1 + 2*eye_hit_box_radius
		dx = dx / max_dist
		dy = dy / max_dist
		inputs.append(dx)
		inputs.append(dy)

		inputs.append(self.cap_zero_to_one(self._owner.health/100.0))
		inputs.append(self.cap_zero_to_one(self._owner.energy/100.0))

		inputs.append(self._brain_data.get("right_wheel_v", 0))
		inputs.append(self._brain_data.get("left_wheel_v", 0))

		# bias neurons ... replaced these with dx and dy of spotted objects in each eye
		#inputs.extend([1, 1, 1, 1])

		# remove all of the brain data in case it isn't updated on next iteration
		self._brain_data.clear()

		# return as inputs for the net
		return inputs

	def kill(self):
		self._owner = None
		self._brain_data.clear()
		self.net = None


	''' Inputs:
	Phase 1
	- right eye( from collision data ) RGB as separate inputs
	- left eye(from collision data) RGB as separate inputs
	- health
	- energy
	- score (add to the score when something good happens e.g., health goes up, energy goes up, movement)
		this can be used for the fitness function or for reinforcement learning
	- wheel velocity from last step (or could let this evolve a recurrent connection)


'''


'''

Phase 2
- direction in the eyes
** energy usage is proportional to velocity
- sound
- smell
- communication
- age ... maybe a component of score?


Outputs
Phase 1
- right wheel velocity
- left wheel velocity

Phase 2
- body color
- emit sound
- emit odor
- communicate

'''