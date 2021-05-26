import ant
import numpy

class Map
	"an environment class"
	def __init__(self,size,walls,food_locations)

	self.size = size
	self.walls = walls
	self.food_locations = food_locations

	"Generate square map of size size"
	self.canvas = np.zeros(size,size)

	"Run perlin noise to generate random pockets of rock"

	"Overlay multiple for cave system gradient"
	"Filter gradient through threshold value for binary open vs solid"
	"Run perlin noise to generate random pockets of food"
	"If open air & food, food @ coordinates"
	"Spawn ant colony"