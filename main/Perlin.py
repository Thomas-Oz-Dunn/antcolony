import numpy as np

def Perlin2D(size,w):
	"Hand made perlin noise in Python"
	square = np.random.rand(size,size)
	
	def interpolate(val0,val1,w):
		return (val1-val0)*((w*(w*6.0-15.0)+10.0)*w*w*w)+val0

	def randomGrad(ix,iy):
		return (x = ,)

	def dotGridGrad(ix,iy,x,y):


