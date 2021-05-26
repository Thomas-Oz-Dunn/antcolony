import ant

class Map
	"an environment class"
	def __init__(self,size,walls,food_locations)

	self.size = size
	self.walls = walls
	self.food_locations = food_locations

	"input dimensions of map"
	"Run perlin noise to generate random pockets of rock"
	"overlay multiple for cave system gradient"
	"assign walls based on border between black and white"
	"Run perlin noise to generate random pockets of food"
	"If open air & food, food @ coordinates"
