import ant
import numpy as np
import perlin

class Map
	"an environment class"
	def __init__(self,size)
		self.size = size

	def GenerateMap(self):
		"Generate square map of size size and random values"
		self.canvas = np.random.rand(self.size,self.size)
		"interpolate"
	

		

	"Overlay multiple for cave system gradient"
	"Filter gradient through threshold value for binary open vs solid"
	"Run perlin noise to generate random pockets of food"
	"If open air & food, food @ coordinates"
	"Spawn ant colony"