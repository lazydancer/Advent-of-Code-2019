import fileinput

def main():
    program = fileinput.input()
    program = [int(i) for i in program[0].split(',')]
    for output in intcode_run(program, []):
        print(output)


def intcode_run(program, inputs):
    inputs = inputs[::-1]
    param = {}
    ptr = 0   
    rb = 0


    print(program)


    program += [0] * 1000



    while program[ptr] is not 99:
        opcode = program[ptr] % 10


        for i in range(1,4): 
            if program[ptr] // int(10**(i+1)) % 10  == 0:
                param[i] = program[ptr + i]
            if program[ptr] // int(10**(i+1)) % 10  == 1:
                param[i] = ptr + i
            if program[ptr] // int(10**(i+1)) % 10  == 2:
                param[i] = rb + program[ptr + i]


        print(ptr, opcode, program[param[1]], program[param[2]], program[param[3]])


        if opcode is 1: 
            program[param[3]] = program[param[1]] + program[param[2]]
            ptr += 4
        elif opcode is 2: 
            program[param[3]] = program[param[1]] * program[param[2]]
            ptr += 4
        elif opcode is 3: 
            program[param[1]] = int(inputs.pop())
            ptr += 2
        elif opcode is 4: 
            yield program[param[1]]
            ptr += 2
        elif opcode is 5 and program[param[1]] or opcode is 6 and not program[param[1]]: 
            ptr = program[param[2]] - 3
            ptr += 3
        elif opcode is 6:
            raise "Number 6"
        elif opcode is 7: 
            program[param[3]] = 1 if program[param[1]] < program[param[2]] else 0
            ptr += 4
        elif opcode is 8: 
            program[param[3]] = 1 if program[param[1]] == program[param[2]] else 0
            ptr += 4
        elif opcode is 9:
            rb = program[param[1]]
            ptr += 2



main()