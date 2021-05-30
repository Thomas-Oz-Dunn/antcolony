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

		"Default nextorient = forward"
		nextorient = self.oriente

		"Conver internal Orientation to Global coordinates"
		self.left, self.center, self.right = o2cart(self.orient,self.location)

		"Random number for decision making"
		ran = np.random.rand(1)

		"If not with food yet"
		if (self.Foodstatus = 0):

			"first, go for food"
			if (world[self.left] = 2 and world[self.center] = 2 and world[self.right] = 2):
				if ran < 0.33:
					if (self.orient = 1): nextorient = 8
					else: nextorient--
				elif ran > 0.33:
					if (self.orient = 8): nextorient = 1
					else: nextorient++
				else: nextorient = self.orient

			elif (world[self.left] = 2 and world[self.center] = 2):
				if ran < 0.5:
					if (self.orient = 1): nextorient = 8
					else: nextorient--
				else: nextorient = self.orient

			elif (world[self.right] = 2 and world[self.center] = 2):
				if ran < 0.5:
					if (self.orient = 8): nextorient = 1
					else: nextorient++
				else: nextorient = self.orient

			elif (world[self.left] = 2 and world[self.right] = 2):
				if ran < 0.5:
					if (self.orient = 1): nextorient = 8
					else: nextorient--
				else:
					if (self.orient = 8): nextorient = 1
					else: nextorient++

			elif (world[self.left] = 2):
				if (self.orient = 1): nextorient = 8
				else: nextorient--

			elif (world[self.right] = 2):
				if (self.orient = 8): nextorient = 1
				else: nextorient++

			elif (world[self.center] = 2):
				nextorient = self.orient

			"second, follow the food trail"
			elif (world[self.left] = 3 and world[self.center] = 3 and world[self.right] = 3):
				if ran < 0.33:
					if (self.orient = 1): nextorient = 8
					else: nextorient--
				elif ran > 0.33:
					if (self.orient = 8): nextorient = 1
					else: nextorient++
				else: nextorient = self.orient

			elif (world[self.left] = 3 and world[self.center] = 3):
				if ran < 0.5:
					if (self.orient = 1): nextorient = 8
					else: nextorient--
				else: nextorient = self.orient

			elif (world[self.right] = 3 and world[self.center] = 3):
				if ran < 0.5:
					if (self.orient = 8): nextorient = 1
					else: nextorient++
				else: nextorient = self.orient

			elif (world[self.left] = 3 and world[self.right] = 3):
				if ran < 0.5: 
					if (self.orient = 1): nextorient = 8
					else: nextorient--
				else:
					if (self.orient = 8): nextorient = 1
					else: nextorient++

			elif (world[self.left] = 3):
				if (self.orient = 1): nextorient = 8
				else: nextorient--

			elif (world[self.right] = 3):
				if (self.orient = 8): nextorient = 1
				else: nextorient++

			elif (world[self.center] = 3):
				nextorient = self.orient

			"without food, third, avoid walls"
			"If left  = wall, nextorient ++"
					"if orient = 8, nextorient = 1"
				"if right = wall, orient --"
					"if orient = 1, orient = 8"
				"if center = wall, nextorient +- 4"

			elif (world[self.left] = 1 and world[self.center] = 1 and world[self.right] = 1):
				nextorient + 4
			elif (world[self.left] = 1 and world[self.center] = 1):

			elif (world[self.right] = 1 and world[self.center] = 1):

			elif (world[self.left] = 1 and world[self.right] = 1):

			elif (world[self.left] = 1):

			elif (world[self.right] = 1):

			elif (world[self.center] = 1):


			"without food, fourth, wander randomly"
			else: 
				if ran < 0.33:
					if (self.orient = 1): nextorient = 8
					else: nextorient--
				elif ran > 0.33:
					if (self.orient = 8): nextorient = 1
					else: nextorient++
				else: nextorient = self.orient

		else:
			"with food, first, follow return trail"
			"with food, second, avoid walls"

	def move(self,world):

		next = search(self,world)

		"Oreint based on next location values"
		l,center,r = o2cart(next,self.x,self.y)

		"previous location"
		previous = [self.x,self.y]

		"Moving forward"
		self.location = center

		"Decrease Energy"
		self.energy--

		"If there be food, grab it"
		if world[self.location] = 2: self.Foodstatus = 1

		"If have food, leave food trail"
		if self.Foodstatus = 1: world[previous] = 3

		"Else leave return trail"
		else: world[previous] = 4

		"Decrement energy"

	"If food, take or eat food, depending on energy level"
	"If no food or food trail, move in random direction forward"
	"If no food, Leave return trail at previous location"
	"If take food, change trail type to food trail"
	"If take food, see environment, find return trail, move to return trail, leave food trail"
	"Drop food off at colony"
	"Eat food to replenish health"
	"Follow food trail back"