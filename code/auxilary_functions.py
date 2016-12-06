def even(x):
	return x % 2  == 0

def odd(x):
	return not even(x)

def divideable_by(number, divider):
	return number % divider == 0

if __name__ == '__main__':
	print(even(20))
	print(odd(20))
	print(odd(5))
	print(even(5))
	print(divideable_by(20, 3))
	print(divideable_by(21, 3))
	print(divideable_by(5, 3))
	print(divideable_by(15, 3))