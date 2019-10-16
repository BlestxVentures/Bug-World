import os
import logging
import pickle
import datetime
import tensorflow as tf
import random

# This module is used for all of the I/O for the simulation.  It manages reading in state, writing out data etc.

# use the directory where the simulation is running
local_dir = os.path.dirname(__file__)

# where the starting config files exist and seed genomes
config_sub_dir = "config"
config_dir = os.path.join(local_dir, config_sub_dir)

# timestamp a subdirectory to store data
log_sub_dir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
log_dir = os.path.join(local_dir, log_sub_dir)

writer = tf.summary.create_file_writer(log_dir)


def get_config_dir():
	"""This where to read the configuration that drives the simulation"""
	# should have the config file(s), any starter genomes
	# execution_dir/config_dir -- have a config dir that can be used many times for several runs

	# initialized in the global scope of this module
	return config_dir


def get_logging_dir():
	"""This where to save data files from the simulation"""

	# initialized in the global scope of this module
	return log_dir


def init_log():
	"""This should be called once to create simulation log directories"""

	# global log variables already set in module
	ld = get_logging_dir()

	# make the necessary subdirectories to store data.  Tensorflow would create these anyway if called first
	try:
		os.makedirs(ld, exist_ok=True)
	except OSError:
		logging.error("Creation of the directory %s failed" % ld)
		exit(-1)
	else:
		logging.info("Successful creation of the directory %s" % ld)


def write_to_log(tag="default", value=0, step=0):
	"""used to encapsulate Tensorboard logging interactions
		tag: name of the scalar metric in Tensorboard
		value: value of the scalar
		step: the step of the simulation that is being logged
	"""
	# writer = tf.summary.create_file_writer(log_dir) is initialized once in global scope of this module

	with writer.as_default():
		tf.summary.scalar(tag, value, step=step)
		writer.flush()


def create_timestamp():
	"""use this to create a unique time stamp based on current time"""
	return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


def get_genome_save_filename(pop_name='Bug'):
	"""construct a file name to save a genome
		pop_name:  default base name
	"""
	# create a unique name for the simulation based on current time
	local_name = pop_name + create_timestamp()
	default_file = os.path.join(get_logging_dir(), local_name)
	return default_file

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
	"""read all of the genome files from a directory"""
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
def test_BugSimState():
	# read a config file
		# 1. file doesn't exist
		# 2. file exists

	# write genomes

	# read genomes
		# 1. file doesn't exist
		# 2. file doesn't contain genome
		# 3. file contains more than one genome
		# 4. read from a list of genome (Phase 2)

	# log fitness values
	# log avg fitness values

	config_file = os.path.join(get_config_dir(), "BugSim.config")
	print(config_file)

	print("Current Logging Dir %s " % get_logging_dir())

	init_log()

	for step in range(10):
		write_to_log(tag="my new metric", value=step, step=step)


if __name__ == "__main__":

	test_BugSimState()




