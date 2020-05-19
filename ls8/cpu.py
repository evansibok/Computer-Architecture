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
        # self.FL = 0 # FL bits: 00000LGE
        self.instructions = {
            # Instructions
            'LDI': 0b10000010,
            'PRN': 0b01000111,
            'HLT': 0b00000001,
            # Arithmetic Operations
            'ADD': 0b10100000,
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

        if op == self.instructions['ADD']:
            self.reg[reg_a] += self.reg[reg_b]
        elif op == self.instructions['SUB']:
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == self.instructions['MUL']:
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == self.instructions['DIV']:
            self.reg[reg_a] /= self.reg[reg_b]
        elif op == self.instructions['INC']:
            self.reg[reg_a] += 1
        elif op == self.instructions['DEC']:
            self.reg[reg_a] -= 1
        elif op == self.instructions['AND']:
            self.reg[reg_a] &= self.reg[reg_b]
        elif op == self.instructions['OR']:
            self.reg[reg_a] |= self.reg[reg_b]
        elif op == self.instructions['NOT']:
            return ~self.reg[reg_a]
        elif op == self.instructions['XOR']:
            self.reg[reg_a] ^= self.reg[reg_b]
        elif op == self.instructions['MOD']:
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
        verify_alu = 0b00100000
        while self.running:
            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            # self.alu(ir, operand_a, operand_b)
            if ir == self.instructions['HLT']:
                self.running = False
                sys.exit(0)
                counter = 1
            elif ir == self.instructions['LDI']:
                self.reg[operand_a] = operand_b
                counter = 3
            elif ir == self.instructions['PRN']:
                value = self.reg[operand_a]
                print(value)
                counter = 2
            elif (ir & verify_alu) == verify_alu:
                self.alu(ir, operand_a, operand_b)
                counter = 3
            self.pc += counter


# Take what you have: the instruction 0b10100000
# then you mask it against what you want: the alu operation bit -
# 0b00100000
# the result: if we have an alu op ? then the result of this masking will be larger than zero, otherwise, if it is zero, it is not an alu operation
# 1010 0000 - ADD
# 0010 0000 - VERIFY VALUE
# ----------
# 0010 0000
# 128  64  32  16  8  4  2  1
# 0     0   1   0  0  0  0  0 - ADD & VERIFY VALUE


# 1010 1000 - AND
# 0010 0000 - 0b00100000
# ---------
# 0010 0000

# If the instruction is ALU it should always return 0b00100000
# if ir & 0b00100000 == 32:
# 1010 1000
# 1010 1000
# ----------
# 1010 1000 -


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
