class Ant:
	"An ant class"
	"All ants start with n energy"
	start_energy = 100

	def __init__(self,location,orient):
		self.location = location
		self.orient = orient
		self.energy = Ant.start_energy
		self.status = "Looking"

	def search(self):
		"See environment of a row of 3 spaces ahead"
		"Detect food or food trail"
		"Detect wall"

	def move(self):
		"Move towards food trail or food plus random wobble"
		"Decrement energy"

	"If food, take or eat food, depending on energy level"
	"If no food or food trail, move in random direction forward"
	"If no food, Leave return trail at previous location"
	"If take food, change trail type to food trail"
	"If take food, see environment, find return trail, move to return trail, leave food trail"
	"Drop food off at colony"
	"Eat food to replenish health"
	"Follow food trail back"