import numpy as np 
import Map.py

class Ant:
	"An ant class"
	"All ants start with 100 energy"
	start_energy = 100

	def __init__(self,x,y,orient):
		"X & Y coordinates"
		self.location = [x,y]

		"Orientation number 1 - 8 w/ 1 = noon, 2 = 45 right"
		self.orient = orient

		"Allocation of energy amount"
		self.energy = Ant.start_energy

		"Boolean food value, 0 false, 1 true"
		self.Foodstatus = 0

	def o2cart(orient,x,y):
		"Define left, center, right"
		switch(orient){
			"N"
			case 1:
				left = [x - 1,y + 1]
				forward = [x,y + 1]
				right = [x + 1,y + 1]
			"NE"
			case 2:
				left = [x,y + 1]
				forward = [x + 1,y + 1]
				right = [x + 1,y]
			"E"
			case 3:
				left = [x + 1,y + 1]
				forward = [x + 1,y]
				right = [x + 1,y - 1]
			"SE"
			case 4:
				left = [x + 1,y]
				forward = [x + 1,y - 1]
				right = [x,y - 1]
			"S"
			case 5:
				left = [x + 1,y - 1]
				forward = [x,y - 1]
				right = [x - 1,y - 1]
			"SW"
			case 6:
				left = [x,y - 1]
				forward = [x - 1 ,y - 1]
				right = [x - 1,y]
			"W"
			case 7:
				left = [x - 1,y - 1]
				forward = [x - 1,y]
				right = [x - 1,y + 1]
			"NW"
			case 8:
				left = [x - 1,y]
				forward = [x - 1,y + 1]
				right = [x - 1,y]
		}

		return left, forward, right

	def search(self,world):
		self.nextorient = self.orient
		self.left, self.center, self.right = o2cart(self.orient,self.location)
		ran = np.random.rand(1)
		if (self.Foodstatus = 0):

			"if not have food, first, go for food"
			if (world[self.left] = 2 and world[self.center] = 2 and world[self.right] = 2):
				if ran < 0.33:
					if (self.orient = 1): self.nextorient = 8
					else: self.nextorient--
				elif ran > 0.33:
					if (self.orient = 8): self.nextorient = 1
					else: self.nextorient++
				else: self.nextorient = self.orient

			elif (world[self.left] = 2 and world[self.center] = 2):
				if ran < 0.5:
					if (self.orient = 1): self.nextorient = 8
					else: self.nextorient--
				else: self.nextorient = self.orient

			elif (world[self.right] = 2 and world[self.center] = 2):
				if ran < 0.5:
					if (self.orient = 8): self.nextorient = 1
					else: self.nextorient++
				else: self.nextorient = self.orient

			elif (world[self.left] = 2 and world[self.right] = 2):
				if ran < 0.5:
					if (self.orient = 1): self.nextorient = 8
					else: self.nextorient--
				else:
					if (self.orient = 8): self.nextorient = 1
					else: self.nextorient++

			elif (world[self.left] = 2):
				if (self.orient = 1): self.nextorient = 8
				else: nextorient--

			elif (world[self.right] = 2):
				if (self.orient = 8): self.nextorient = 1
				else: self.nextorient++

			elif (world[self.center] = 2):
				self.nextorient = self.orient

			"if not have food, second, follow the food trail"
			elif (world[self.left] = 3 and world[self.center] = 3 and trailmap[self.right] = 3):
				if ran < 0.33:
					if (self.orient = 1): self.nextorient = 8
					else: self.nextorient--
				elif ran > 0.33:
					if (self.orient = 8): self.nextorient = 1
					else: self.nextorient++
				else: self.nextorient = self.orient

			elif (world[self.left] = 3 and world[self.center] = 3):
				if ran < 0.5:
					if (self.orient = 1): self.nextorient = 8
					else: self.nextorient--
				else: self.nextorient = self.orient

			elif (world[self.right] = 3 and world[self.center] = 3):
				if ran < 0.5:
					if (self.orient = 8): self.nextorient = 1
					else: self.nextorient++
				else: self.nextorient = self.orient

			elif (world[self.left] = 3 and world[self.right] = 3):
				if ran < 0.5: 
					if (self.orient = 1): self.nextorient = 8
					else: self.nextorient--
				else:
					if (self.orient = 8): self.nextorient = 1
					else: self.nextorient++

			elif (world[self.left] = 3):
				if (self.orient = 1): self.nextorient = 8
				else: nextorient--

			elif (world[self.right] = 3):
				if (self.orient = 8): self.nextorient = 1
				else: self.nextorient++

			elif (world[self.center] = 3):
				self.nextorient = self.orient

			"without food, third, avoid walls"
				"If left  = wall, nextorient ++"
					"if orient = 8, nextorient = 1"
				"if right = wall, orient --"
					"if orient = 1, orient = 8"
				"if center = wall, nextorient +- 4"

			"if 2 or 3 directions, random from true, always perpindicular"

			"without food, fourth, wander randomly"

		"with food, first, follow return trail"
		"with food, second, avoid walls"

	def move(self,world):
		"Oreint based on next location values"
		l,center,r = o2cart(self.nextorient,self.x,self.y)

		"Moving forward"
		self.location = center

		"Decrease Energy"
		self.energy--

		"If there be food, grab it"
		if world[self.location] = 2: self.Foodstatus = 1

		"If have food, leave food trail"
		if self.Foodstatus = 1: world[self.location] = 3

		"Else leave return trail"
		else: world[self.location] = 4

		"leave a trail behind"

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