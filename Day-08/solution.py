import fileinput

WIDTH = 25
HEIGHT = 6

transmission = fileinput.input()[0].strip()

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

layers = chunks(transmission, WIDTH * HEIGHT)

fewest_zeros, _ = min([(l, l.count("0")) for l in layers], key=lambda x: x[1])

print('The solution to part 1 is:', fewest_zeros.count('1') * fewest_zeros.count('2'))


def get_color(layers, i):
	for l in layers:
		if l[i] == '1':
			return '1'
		if l[i] == '0':
			return '0'

layers = list(chunks(transmission, WIDTH * HEIGHT))

img = []
for i in range(WIDTH * HEIGHT):
	color = get_color(layers, i)
	img.append(color)
	
for r in range(HEIGHT):
    print(''.join(img[r * WIDTH:(r + 1) * WIDTH]).replace('0', ' ').replace('1', 'x'))
