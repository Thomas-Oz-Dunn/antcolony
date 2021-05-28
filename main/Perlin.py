import numpy as np

def Perlin(x,y):
	"Hand made perlin noise in Python"

	def interpolate(a0,a1,w):
		return (a1 - a0) * ((w * (w * 6.0 - 15.0) + 10.0) * w * w * w) + a0

	def dotGridGrad(ix,iy,x,y):
		vec = np.random.rand(1)
		gradient = (x = cos(vec), y = sin(vec))
		dx = x - ix
		dy = y - iy
		return dx*gradient.x + dy*gradient.y

	x0 = x
	x1 = x0++ 
	y0 = y
	y1 = y0++

	sx = x - x0
	sy = y - y0

	n0 = dotGridGrad(x0,y0,x,y)
	n1 = dotGridGrad(x1,y0,x,y)
	ix0 = interpolate(n0,n1,sx)

	n0 = dotGridGrad(x0,y1,x,y)
	n1 = dotGridGrad(x1,y1,x,y)
	ix1 = interpolate(n0,n1,sx)	

	value = interpolate(ix0,ix1,sy)
	return value

Perlin(1,6)