import fileinput
import copy
import math

def main():
	asteroids = set()
	for y, line in enumerate(fileinput.input()):
		line = line.strip()
		for x, char in enumerate(line):
			if char == '#':
				asteroids.add((x, y))

	solution = max([visible_asteroids(ast, asteroids) for ast in asteroids])
	print("The solution to part 1 is", solution)


def visible_asteroids(ast, asteroids):
	local_asteroids = copy.copy(asteroids)
	space_width = max(asteroids)[0] * 2

	top_lefts = [(ast[0]-x, ast[1]-x) for x in range(space_width)]
	
	for i, tl in enumerate(top_lefts):
		width = i*2+1
	
		casts_shade = local_asteroids.intersection(ring(tl, width))

		for cs in casts_shade:
			shaded = shade_mapping(ast, cs, space_width)
			local_asteroids -= shaded


	return len(local_asteroids)



def shade_mapping(c, b, width):
	x_offset = b[0] - c[0]
	y_offset = b[1] - c[1]
	
	gcd = math.gcd(x_offset, y_offset)

	if gcd != 0:
		x_offset = int(x_offset / gcd)
		y_offset = int(y_offset / gcd)

	shaded = set()
	for i in range(1, width):
		shaded.add((b[0] + x_offset * i, b[1] + y_offset * i))

	return shaded


def ring(tl_loc, width):
	x, y = tl_loc

	result = set()

	for i in range(width):
		result.add((tl_loc[0] + i, tl_loc[1]))
	for i in range(1, width):
		result.add((tl_loc[0] + width-1, tl_loc[1] + i))
	for i in range(1, width):
		result.add((tl_loc[0] + width-1 - i, tl_loc[1] +  width-1))
	for i in range(1, width-1):
		result.add((tl_loc[0], tl_loc[1] + width-1 - i))

	return result

main()