import fileinput
from itertools import permutations
import copy

INPUT = 1

def main():
    int_program = load_program()
    INPUT = 1
    print('The solution to part 1 is', run_program(int_program)) # 4930687
    INPUT = 5
    print('The solution to part 2 is', run_program(int_program)) # 5335


def load_program():
    int_program = fileinput.input()[0]
    int_program = int_program.split(',')     
    int_program = list(map(int, int_program))
    return int_program

def run_program(input_int_program):
    int_program = copy.copy(input_int_program)

    pointer = 0
    while int_program[pointer] != 99:

        old_pointer = copy.copy(pointer)

        (int_program, pointer) = run_opcode(int_program, pointer)

        if old_pointer == pointer:
            if int_program[pointer] % 10 in [1, 2, 7, 8]:
                pointer += 4
            elif int_program[pointer] % 10 in [5, 6]:
                pointer += 3
            elif int_program[pointer] % 10 in [3, 4]:
                pointer += 2


    return int_program[0]


def run_opcode(int_program, pointer):
    opcode = int_program[pointer]

    first = int_program[pointer+1] 
    second = int_program[pointer+2]
    third = int_program[pointer+3]

    first_parameter_mode = int((opcode % 1000 - opcode % 100) / 100) 
    second_parameter_mode = int((opcode % 10000 - opcode % 1000) / 1000)

    if(first_parameter_mode == 0):
        a = int_program[first]
    else:
        a = first

    if(second_parameter_mode == 0):
        b = int_program[second]
    else:
        b = second


    if opcode % 10 == 1:
        int_program[third] = a + b

    elif opcode % 10 == 2:
        int_program[third] = a * b

    elif opcode % 10 == 3:
        int_program[first] = INPUT 

    elif opcode % 10 == 4:
        print("---------- TEST diagnotic program output:", int_program[first])

    elif opcode % 10 == 5:
        if a != 0:
            pointer = b

    elif opcode % 10 == 6:
        if a == 0:
            pointer = b 

    elif opcode % 10 == 7:
        if a < b:
            int_program[third] = 1
        else:
            int_program[third] = 0

    elif opcode % 10 == 8:
        if a == b:
            int_program[third] = 1
        else:
            int_program[third] = 0
    else:
        raise Error()

    return (int_program, pointer)

main()