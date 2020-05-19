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

    def __repr__(self):
        return f""

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def load(self, filename):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00000001,  # HLT
        # ]

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
            print("file not found!!!")
            sys.exit(2)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == = ""
        # elif op == "SUB": etc
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
            self.pc += counter


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
