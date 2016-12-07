
class coordinate:
	x = 0
	y = 0

	def __init__(self, **kwargs):
		keys = kwargs.keys()
		if 'x' in keys:
			self.x = kwargs['x']
		if 'y' in keys:
			self.y = kwargs['y']

	def __str__(self):
		return 'x : %s\ty: %s' %(self.x, self.y)


if __name__ == '__main__':
	P = coordinate()
	print(P)
	P = coordinate(x=2)
	print(P)
	P = coordinate(y=3)
	print(P)
	P = coordinate(x=5, y=7)
	print(P)

