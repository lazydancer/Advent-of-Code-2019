import fileinput
import numpy as np

asteroids = set()
for y, line in enumerate(fileinput.input()):
	line = line.strip()
	for x, char in enumerate(line):
		if char == '#':
			asteroids.add((x, y))


max_angles = 0
max_ast = (0,0)

for from_ast in asteroids:
	angles = set()
	for to_ast in asteroids:

		if from_ast == to_ast:
			continue

		x, y = (to_ast[0] - from_ast[0], to_ast[1] - from_ast[1])

		angles.add(np.angle(np.complex(x, y)))

	if len(angles) > max_angles:
		max_angles = len(angles)
		max_ast = from_ast 
	

print('The solution to part 1 is', max_angles, 'on asteroid', max_ast)


ast_angle_distance = []

for to_ast in asteroids:

	if to_ast == max_ast:
		continue

	x, y = (to_ast[0] - max_ast[0], to_ast[1] - max_ast[1])
	angle = np.angle(np.complex(x, y), deg=True)
	distance = np.absolute(np.complex(x,y))

	ast_angle_distance.append((to_ast, angle, distance))



rotated = []
for a in ast_angle_distance:
	angle = a[1]

	angle += 90

	if angle < 0:
		angle += 360

	if angle == 0:
		angle = 360

	rotated.append((a[0], angle, a[2]))


rotated.sort(key=lambda x: x[1], reverse=True)


updated_rotated = rotated
count = 0

for cycle in range(10):
	
	seen_angle = set()
	rotated = updated_rotated
	updated_rotated = []

	for ast in rotated:
		if ast[1] not in seen_angle:			
			seen_angle.add(ast[1])
			count += 1

			print(count, ast)

			if count == 201:
				print('The solution to Part 2 is', ast[0][0] * 100 + ast[0][1])
		else:
			updated_rotated.append(ast)


	print(cycle, updated_rotated)

	# 2135 too high
	# 1937 too high
	# 1738 too high 