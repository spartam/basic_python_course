functions = set()

def decorator(command):
	def new_func(self, *args, **kwargs):
		print('executed %s with:\n\targuments %s\n\tkeywordarguments %s' % (command.__name__, args, kwargs))
		command(self, *args, **kwargs)
	functions.add((command.__name__, command))
	return new_func



@decorator
def add(x, y):
	return x + y

add(5, 3)
print(functions)



