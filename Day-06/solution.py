import fileinput


input = fileinput.input()
input = [line.strip().split(')') for line in input]

# hash guide from planet to lower orbit 
guide = {line[1]: line[0] for line in input}

# should be only one planet that doesn't have a guide value
(base,) = set(guide.values()) - set(guide.keys())

count = 0
for planet in guide:
	while planet != base:
		planet = guide[planet]
		count += 1


print('The solution to part 1 is:', count) # 162816


# Find the descent patterns of YOU and SAN
# Match the first common element
# Add up the above to find the transfer distance - 2
you_path = []
planet = 'YOU'
while planet != base:
	planet = guide[planet]
	you_path.append(planet)
you_path.reverse()

san_path = []
planet = 'SAN'
while planet != base:
	planet = guide[planet]
	san_path.append(planet)
san_path.reverse()

diverge_step = 0
for step in range(len(san_path)):
	if san_path[step] != you_path[step]:
		diverge_step = step - 1
		break;


steps_you = len(you_path) - diverge_step 
steps_san = len(san_path) - diverge_step

result = steps_san + steps_you - 2

print('The solution to part 2 is:', result)
