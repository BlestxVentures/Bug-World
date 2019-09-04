import os
import logging
import pickle

# This module is used for all of the I/O for the simulation.  It manages reading in state, writing out data etc.

data_file_version = '1.0'  # used to change version when file format changes.

def sim_version():  # used to tie simulation version to the data it produces
	pass

def config_director():  # where to read the configuration that drives the simulation
	"""this can be used to store several different configs that would drive a scheduler"""
	pass


def logging_directory():
	pass


def write_to_log():
	# hook into the default reporter set to write to the log file
	# should be in the data directory
	pass


def data_directory():

	# create a unique data directory for each simulation
	def create(): # construct the path for where to read write data for a simulation based on start time, process id?
		pass


def create_timestamp():
	"""use this to create a unique time stamp based on current time"""
	# is there some standard lib that already does this? Yes datetime
	pass


def write_genome_state():

	# create a file name for the best genome

	def get_file_name(pop_name='Bug'):  # construct a file name to load or save a genome
		# create a unique name for the simulation based on start time
		# put data in filename for easy searching, like date time, generation, fitness

		# create a file to store the best bug in the population
		local_name = pop_name + '-winner'
		local_dir = os.path.dirname(__file__)
		default_winner_file = os.path.join(local_dir, local__name)
		return default__file

	def write_genome():  # write a single genome to a file and related data
		"""genome, generation, fitness, bug_type, config file used to describe genome"""
		# fitness should be normalized
		# should have a file version information so can match data to simulation version?
		pass

	def read_genome():  # read a single genome in from a file and related data
		"""see write_genome"""
		# check data file version to see if it matches the code so that the correct code is used to read in the file
		# assert the data read in matches DefaultGenome
		pass

	def read_genomes():
		# should create a dictionary of all of the data

		pass

	def create_population_dict():
		# take full dictionary of data read in and then create a valid population out of it
		# {key:genome}
		pass

	def create_population_from_file():
		"""probably belongs on the BugPopulation class"""
		# read in a bunch of genomes
		# reset their keys
		# put them in a dict
		# reset the indexer of the population
		pass

	def write_genomes():
		pass

	def reset_key():
		pass

	def write_config():
		"""should store the config associated with the genome once"""

	def read_all_genomes():
		'''read all of the genome files from a directory'''
		# get a list of the files
		# filter by name
		# use read_genome one at a time
		# assert the format of the pickle


def genome_to_vec(genome):

	# take genome and flatten to a vector that could be save to a table or file (use Pandas?)
	# maybe use zeros for fully connected for a sparse net?
	# should use OrderedDict so all genomes are output the same
	pass


# ------------------- TEST CODE ------------------------------
if __name__ == "__main__":

	# create a directory
	# create a bad directory name and try to I/O
	# write genomes
	# read genomes

	pass



