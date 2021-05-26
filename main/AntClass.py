import numpy as np 

class Ant:
	"An ant class"
	"All ants start with 100 energy"
	start_energy = 100

	def __init__(self,x,y,orient):

		"X & Y coordinates"
		self.x = x
		self.y = y

		"Orientation number 1 - 8 w/ 1 = noon, 2 = 45 right"
		self.orient = orient

		"Allocation of energy amount"
		self.energy = Ant.start_energy

		"Boolean food value, 0 false, 1 true"
		self.Foodstatus = 0

	def search(self):
		"See environment of a row of 3 spaces ahead"
		"Detect food or food trail"
		"Detect wall"

		"Define left, center, right"
		switch(self.orient){
			"N"
			case 1:
				self.left = (self.x - 1,self.y + 1)
				self.forward = (self.x,self.y + 1)
				self.right = (self.x + 1,self.y + 1)
			"NE"
			case 2:
				self.left = (self.x,self.y + 1)
				self.forward = (self.x + 1,self.y + 1)
				self.right = (self.x + 1,self.y)
			"E"
			case 3:
				self.left = (self.x + 1,self.y + 1)
				self.forward = (self.x + 1,self.y)
				self.right = (self.x + 1,self.y - 1)
			"SE"
			case 4:
				self.left = (self.x + 1,self.y)
				self.forward = (self.x + 1,self.y - 1)
				self.right = (self.x,self.y - 1)
			"S"
			case 5:
				self.left = (self.x + 1,self.y - 1)
				self.forward = (self.x,self.y - 1)
				self.right = (self.x - 1,self.y - 1)
			"SW"
			case 6:
				self.left = (self.x,self.y - 1)
				self.forward = (self.x - 1 ,self.y - 1)
				self.right = (self.x - 1,self.y)
			"W"
			case 7:
				self.left = (self.x - 1,self.y - 1)
				self.forward = (self.x - 1,self.y)
				self.right = (self.x - 1,self.y + 1)
			"NW"
			case 8:
				self.left = (self.x - 1,self.y)
				self.forward = (self.x - 1,self.y + 1)
				self.right = (self.x - 1,self.y)
		}

		"if Foodstatus = 0"
		"first, go for food"
		"If left  = food, orient --"
			"if orient = 0, orient = 8"
		"if right = food, orient ++"
			"if orient = 9, orient = 1"
		"if center = food, constant"
		"if 2 or 3 directions, random from true"

		"second, follow the trail"
		"If left  = foodtrail, orient --"
			"if orient = 0, orient = 8"
		"if right = foodtrail, orient ++"
			"if orient = 9, orient = 1"
		"if center = foodtrail, constant"
		"if 2 or 3 directions, random from true"

		"third, avoid walls"
		"If left  = wall, orient ++"
			"if orient = 0, orient = 8"
		"if right = wall, orient --"
			"if orient = 9, orient = 1"
		"if center = wall, orient +- 1"
		"if 2 or 3 directions, random from true, always perpindicular"

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