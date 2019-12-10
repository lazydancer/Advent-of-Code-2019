import fileinput
from itertools import permutations

def main():
    program = fileinput.input()
    program = [int(i) for i in program[0].split(',')]

    highest = 0
    for phase_settings in permutations(range(0,5), 5):
        output = 0
        for phase in phase_settings:
            output = next(intcode_run(program, [phase, output]))
        
        highest = output if output > highest else highest

    print("The solution to part 1 is", highest)



def intcode_run(program, inputs):
    inputs = inputs[::-1]
    param = {}
    ptr = 0   
    skip = (4,4,2,2,3,3,4,4)

    while program[ptr] is not 99:
        opcode = program[ptr] % 10
        for i in range(1,4): 
            param[i] = ptr + i if program[ptr]//int('100'.ljust(i+2, '0')) % 10 else program[ptr + i]
        if opcode is 1: 
            program[param[3]] = program[param[1]] + program[param[2]]
        elif opcode is 2: 
            program[param[3]] = program[param[1]] * program[param[2]]
        elif opcode is 3: 
            program[param[1]] = int(inputs.pop())
        elif opcode is 4: 
            yield program[param[1]]
        elif opcode is 5 and program[param[1]] or opcode is 6 and not program[param[1]]: 
            ptr = program[param[2]] - 3
        elif opcode is 7: 
            program[param[3]] = 1 if program[param[1]] < program[param[2]] else 0
        elif opcode is 8: 
            program[param[3]] = 1 if program[param[1]] == program[param[2]] else 0
        ptr += skip[opcode-1]

main()