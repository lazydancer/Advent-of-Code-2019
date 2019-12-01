import fileinput

def part_1():
	module_weights = map(int, fileinput.input())
	fuel_calc = lambda x: x // 3 - 2

	return sum(map(fuel_calc, module_weights))	

def part_2():
	module_weights = map(int, fileinput.input())

	return sum(map(calculate_fuel, module_weights))

def calculate_fuel(module_weight):
	total_fuel = 0
	w = module_weight

	while w >= 9:
		w = w // 3 - 2
		total_fuel += w

	return total_fuel

print('The solution to part 1 is', part_1()) # 3188480
print('The solution to part 2 is', part_2()) # 4779847
