import fileinput
from itertools import permutations
import copy

def main():
    int_program = load_program()
    print('The solution to part 1 is', run_program(int_program, 12, 2)) # 4930687
    print('The solution to part 2 is', find_inputs(int_program, 19690720)) # 5335


def load_program():
    int_program = fileinput.input()[0]
    int_program = int_program.split(',')     
    int_program = list(map(int, int_program))
    return int_program


def find_inputs(int_program, value):
    for noun, verb in permutations(range(100), 2):
        if run_program(int_program, noun, verb) == value:
            return 100 * noun + verb


def run_program(input_int_program, noun, verb):
    int_program = copy.copy(input_int_program)

    int_program[1] = noun
    int_program[2] = verb

    for i in range(0, len(int_program), 4):
        if isComplete(int_program, i):
            break

        int_program = run_opcode(int_program, i)

    return int_program[0]


def run_opcode(int_program, i):
    opcode = int_program[i]
    first = int_program[i+1]
    second = int_program[i+2]
    result = int_program[i+3]

    if opcode == 1:
        int_program[result] = int_program[first] + int_program[second]
    elif opcode == 2:
        int_program[result] = int_program[first] * int_program[second]
    else:
        raise Error()

    return int_program


def isComplete(int_program, i):
    return int_program[i] == 99


main()