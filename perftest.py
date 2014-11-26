# Run this with and without the patch applied, to see the performance
# impact of the exception conversions.

def gen(depth):
	if depth:
		g=gen(depth-1)
		try:
			while True:
				yield next(g)
		except StopIteration:
			return
	yield 1
	yield 2
	yield 3

for i in range(100000):
	if tuple(gen(100)) != (1,2,3): raise SystemError
