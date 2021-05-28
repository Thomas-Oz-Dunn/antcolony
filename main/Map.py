import ant
import numpy as np
import perlin

class Map
	"an environment class"
	def __init__(self,size)
		self.size = size

	def GenerateMap(self):
		"Generate square map of size size and random values"
		self.canvas = numpy.zeros(self.size,self.size)
		for i in range(1,self.size):
			for j in range(1,self.size):
				self.canvas[i,j] = Perlin(i,j)
				if self.canvas[i,j] < 0.5 :
					"Open"
					self.canvas[i,j] = 0
				else:
					"Wall"
					self.canvas[i,j] = 1

	

		

	"Overlay multiple for cave system gradient"
	"Filter gradient through threshold value for binary open vs solid"
	"Run perlin noise to generate random pockets of food"
	"If open air & food, food @ coordinates"
	"Spawn ant colony"