import ant
import numpy

class Map
	"an environment class"
	def __init__(self,size)
		self.size = size

	"Generate square map of size size"
	self.canvas = np.zeros(self.size,self.size)


	"Run perlin noise to generate random pockets of rock"
	def GenerateCave(self)

	"Overlay multiple for cave system gradient"
	"Filter gradient through threshold value for binary open vs solid"
	"Run perlin noise to generate random pockets of food"
	"If open air & food, food @ coordinates"
	"Spawn ant colony"