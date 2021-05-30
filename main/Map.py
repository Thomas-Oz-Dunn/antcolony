import ant
import numpy as np
import perlin

class Map
	"an environment class"
	def __init__(self,size)
		self.size = size

	def GenerateMap(self):
		"Generate square map of size size and random values"
		canvas = numpy.zeros(self.size,self.size)
		for i in range(1,self.size):
			for j in range(1,self.size):
				canvas[i,j] = Perlin(i,j)
				if canvas[i,j] < 0.5 :
					"Open"
					canvas[i,j] = 0
				elif canvas[i,j] > 0.5:
					"Walls"
					canvas[i,j] = 1
				else:
					canvas[i,j] = 2
		return canvas

	
	"Overlay multiple for cave system gradient"
	"Filter gradient through threshold value for binary open vs solid"
	"Run perlin noise to generate random pockets of food"
	"If open air & food, food @ coordinates"
	"Spawn ant colony"
	"Trail dissipation over time"