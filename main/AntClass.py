class Ant:
	"an ant class"
	def __init__(self,foodstatus,location,energy)

		self.foodstatus = foodstatus
		self.location = location
		self.energy = energy

		"See environment of a row of 3 spaces ahead"
		"Detect food or food trail"
		"Detect wall"
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