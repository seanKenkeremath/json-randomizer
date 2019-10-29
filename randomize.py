import json
import sys
import os
from random import random
from random import randint

path_list = []


def main():
	file_path = sys.argv[1]
	randomness = float(sys.argv[2])
	output_file_path = file_path
	if len(sys.argv) > 3:
		output_file_path = sys.argv[3]
	with open(file_path) as json_file:
		data = json.load(json_file)
		randomize(data, randomness, [])
		dirname = os.path.dirname(output_file_path)
		if not os.path.exists(dirname):
			os.makedirs(dirname)
		with open(output_file_path, 'w') as outfile:
			json.dump(data, outfile)
		with open(output_file_path + ".paths.txt", 'w') as path_outfile:
			for i in range (0, len(path_list)):
				path_outfile.write(path_list[i])
				path_outfile.write("\n\n")
			path_outfile.close()

def randomize(json_object, randomness, path):
	if isinstance(json_object, list):
		for i in range(0, len(json_object)):
			path.append(i)
			child = json_object[i]
			if isLeaf(child):
				handleLeaf(json_object, i, randomness, path)
			else:
				randomize(child, randomness, path)
			del path[-1]
	elif json_object is None:
		return
	else:
		for key in json_object:
			path.append(key)
			child = json_object[key]
			if isLeaf(child):
				handleLeaf(json_object, key, randomness, path)
			else:
				randomize(child, randomness, path)
			del path[-1]

def handleLeaf(parent, key, randomness, path):
	random_num = random()
	if (random_num < randomness):
		original = parent[key]
		parent[key] = getRandomValue(parent[key], random_num/randomness)
		new = parent[key]
		path_list.append(formatPath(path, original, new))

def getRandomValue(leaf, rand_percent):
	if (isinstance(leaf, str)):
		if (rand_percent < 0.25):
			return None
		elif (rand_percent < 0.5):
			return ""
		else:
			return "random"
	if (isinstance(leaf, bool)):
		if (rand_percent < 0.5):
			return False
		else:
			return True
	if (isinstance(leaf, int)):
		return randint(-5000, 5000)
	if (isinstance(leaf, float)):
		return random() * randint(-5000, 5000)


def formatPath(path, original, new):
	formatted = ""
	for i in range (0, len(path)):
		formatted += "/" + str(path[i])
	formatted += " (" + str(original) + " -> " + str(new) + ") "
	return formatted

def isLeaf(json_object):
	return isinstance(json_object, (str, int, float, bool))
 
if __name__ == "__main__":
    main()