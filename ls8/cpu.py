"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.running = True
        self.LDI = 0b10000010
        self.PRN = 0b01000111
        self.HLT = 0b00000001
        self.arith = {'ADD': 0b10100000,
                      'SUB': 0b10100001,
                      'MUL': 0b10100010,
                      'DIV': 0b10100011,
                      'INC': 0b01100101,
                      'DEC': 0b01100110,
                      'AND': 0b10101000,
                      'OR': 0b10101010,
                      'NOT': 0b01101001,
                      'XOR': 0b10101011,
                      'SHL': 0b10101100,
                      'SHR': 0b10101101,
                      'MOD': 0b10100100,
                      'CMP': 0b10100111, }

    def __repr__(self):
        return f""

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def load(self, filename):
        """Load a program into memory."""

        address = 0

        try:
            with open(filename) as file:
                for line in file:
                    # remove comments
                    no_comments = line.split('#')

                    # Grab the numbers and remove whitespaces
                    numbers = no_comments[0].strip()

                    # If we have an empty line
                    if numbers == '':
                        # continue iteration
                        continue

                    # Convert to integers to make it possible
                    # to save to register
                    values = int(numbers, 2)

                    # Using the address as index
                    # store the result gotten from reading the file
                    # and save to self.reg[address]
                    self.ram[address] = values

                    # Continue iteration
                    address += 1
        except FileNotFoundError:
            print("File not found!!!")
            sys.exit(2)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == self.arith['ADD']:
            self.reg[reg_a] += self.reg[reg_b]
        elif op == self.arith['SUB']:
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == self.arith['MUL']:
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == self.arith['DIV']:
            self.reg[reg_a] /= self.reg[reg_b]
        elif op == self.arith['INC']:
            self.reg[reg_a] += 1
        elif op == self.arith['DEC']:
            self.reg[reg_a] -= 1
        elif op == self.arith['AND']:
            self.reg[reg_a] &= self.reg[reg_b]
        elif op == self.arith['OR']:
            self.reg[reg_a] |= self.reg[reg_b]
        elif op == self.arith['NOT']:
            return ~self.reg[reg_a]
        elif op == self.arith['XOR']:
            self.reg[reg_a] ^= self.reg[reg_b]
        elif op == self.arith['SHL']:
            new_value = self.reg[reg_a] << self.reg[reg_b]
            return new_value
        elif op == self.arith['SHR']:
            new_value = self.reg[reg_a] >> self.reg[reg_b]
            return new_value
        elif op == self.arith['MOD']:
            self.reg[reg_a] %= self.reg[reg_b]
        # elif op == 'CMP':
        #     if self.reg[reg_a] == self.reg[reg_b]:
        #         E = 1
        #     else:
        #         E = 0

        #     if self.reg[reg_a] < self.reg[reg_b]:
        #         L = 1
        #     else:
        #         L = 0

        #     if self.reg[reg_a] > self.reg[reg_b]:
        #         G = 1
        #     else:
        #         G = 0
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        counter = 0
        while self.running:
            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            # self.alu(ir, operand_a, operand_b)
            if ir == self.HLT:
                self.running = False
                sys.exit(0)
                counter = 1
            elif ir == self.LDI:
                self.reg[operand_a] = operand_b
                counter = 3
            elif ir == self.PRN:
                value = self.reg[operand_a]
                print(value)
                counter = 2
            elif ir == self.arith['MUL']:
                self.alu(ir, operand_a, operand_b)
                counter = 3
            self.pc += counter


# Get key and value
# for key in dictionary
# if value == dictionary['MUL']


# def load_dict(dict_items):
#     count = 0
#     for k, v in dict_items.items():
#         if v == dict_items['MUL']:
#             print('mul', k)
#             return k
#         count += 1


# arith = {'ADD': 0b10100000,
#          'SUB': 0b10100001,
#          'MUL': 0b10100010,
#          'DIV': 0b10100011,
#          'INC': 0b01100101,
#          'DEC': 0b01100110,
#          'AND': 0b10101000,
#          'OR': 0b10101010,
#          'NOT': 0b01101001,
#          'XOR': 0b10101011,
#          'SHL': 0b10101100,
#          'SHR': 0b10101101,
#          'MOD': 0b10100100,
#          'CMP': 0b10100111, }

# print(load_dict(arith))


# Implement three instructions:

# LDI: load "immediate", store a value in a register, or "set this register to this value".
# PRN: a pseudo - instruction that prints the numeric value stored in a register.
# HLT: halt the CPU and exit the emulator.

# Not Implemented
# run()
# pc
# ram
# ram_read()
# ram_write()
# register (reg)

# cpu.py -> Implements the 8bit computer architecture
# Implemented

# ls8.py -> Run with each example file as second argument to run the program created in cpu.py
# LS8-spec ->
#

# Start by reading LS8-spec.md
