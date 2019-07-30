import os
import pickle
import visualize
import neat
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


def load_winner():
	local_winner_name = 'HERB' + '-winner'
	local_dir = os.path.dirname(__file__)
	default_winner_file = os.path.join(local_dir, local_winner_name)

	with open(default_winner_file, 'rb') as f:
		winner = pickle.load(f)

	return winner


def load_config():
	# Load the config file, which is assumed to live in
	# the same directory as this script.
	local_dir = os.path.dirname(__file__)
	config_path = os.path.join(local_dir, 'BUG-config-ff')
	config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
						 neat.DefaultSpeciesSet, neat.DefaultStagnation,
						 config_path)
	return config


def visualize_bug(config, winner):

	node_names = {-1: 'rr', -2: 'rg', -3: 'rb', -4: 'lr', -5: 'rg', -6: 'rg', -7: 'h', -8: 'e', -9: 'vr', -10: 'vl'}
	node_names.update({-11: 'vro', -12: 'vlo', -13: 'vr', -14: 'vl'})
	node_names.update({0: 'vr', 1: 'vl'})

	visualize.draw_net(config, winner, True, node_names=node_names)

	visualize.draw_net(config, winner, view=True, node_names=node_names, filename="winner.gv")
	visualize.draw_net(config, winner, view=True, node_names=node_names, filename="winner-enabled.gv", show_disabled=False)
	visualize.draw_net(config, winner, view=True, node_names=node_names, filename="winner-enabled-pruned.gv", show_disabled=False, prune_unused=True)


if __name__ == "__main__":
	winner = load_winner()
	config = load_config()
	visualize_bug(config, winner)
