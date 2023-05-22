import re

class Interpreter:
    def __init__(self):
        self.symbol_table = {}
        self.tokens = []
        self.line_number = 0

    def tokenize(self, code):
        self.tokens = re.findall("\s*(---|-|\+\+|--|[A-Za-z_][A-Za-z0-9_]*|\d+|\S)\s*", code)

    def get_next_token(self):
        return self.tokens.pop(0) if self.tokens else None

    def parse_assignment(self):
        identifier = self.get_next_token()
        if self.get_next_token() != '=':
            return 'error', self.line_number
        if self.tokens and self.tokens[0] == ';':
            self.symbol_table[identifier] = None  # Assign None for simple assignment without expression
            self.get_next_token()  # Consume the semicolon
            return None, self.line_number
        expr_value, error_line = self.parse_expr()
        if expr_value == 'error' or not self.tokens or self.tokens[0] != ';':
            return 'error', error_line
        self.symbol_table[identifier] = expr_value
        return self.get_next_token(), self.line_number  # Return the semicolon

    def parse_expr(self):
        negations = 0
        while self.tokens and self.tokens[0] == '---':
            negations += 1
            self.get_next_token()  # consume '---'
        value, error_line = self.parse_term()
        if value == 'error':
            return 'error', error_line
        if negations % 2 == 1:
            value = -value
        while self.tokens and self.tokens[0] in ['+', '-']:
            op = self.get_next_token()
            rhs, error_line = self.parse_term()
            if rhs == 'error':
                return 'error', error_line
            if op == '+':
                value += rhs
            else:
                value -= rhs
        return value, error_line

    def parse_term(self):
        value, error_line = self.parse_fact()
        while self.tokens and self.tokens[0] == '*':
            self.get_next_token()  # consume '*'
            rhs, error_line = self.parse_fact()
            if rhs == 'error':
                return 'error', error_line
            value *= rhs
        return value, error_line

    def parse_fact(self):
        negations = 0
        while self.tokens and self.tokens[0] in ['-', '+', '++', '--']:
            token = self.get_next_token()
            if token == '-':
                negations += 1
            elif token == '+':
                negations -= 1
            elif token == '++':
                continue
            elif token == '--':
                negations += 2

        token = self.get_next_token()
        if token.isdigit():
            if token != '0' and token.lstrip('0') != token:
                return 'error', self.line_number
            value = int(token)
        elif token.isidentifier():
            if token not in self.symbol_table:
                return 'error', self.line_number
            value = self.symbol_table[token]
        elif token == '(':
            value, error_line = self.parse_expr()
            if not self.tokens or self.get_next_token() != ')':
                return 'error', error_line
        else:
            return 'error', self.line_number

        while self.tokens and self.tokens[0] == '/':
            self.get_next_token()  # consume '/'
            rhs, error_line = self.parse_fact()
            if rhs == 'error':
                return 'error', error_line
            if rhs == 0:
                print(f'Division by zero in line {self.line_number}')
                return 'error', self.line_number
            value /= rhs

        return -value if negations % 2 else value, self.line_number

    def interpret(self, code):
        self.symbol_table.clear()  # Clear the symbol table before each interpretation
        self.line_number = 0
        for line in code.splitlines():
            self.line_number += 1
            self.tokenize(line.strip())
            result, error_line = self.parse_assignment()
            if result == 'error':  # Check for errors in assignment
                print(f'Error in line {error_line}: {line}')
                return
        for var, val in self.symbol_table.items():
            print(f'{var} = {val}')

interpreter = Interpreter()


def process_hardcoded_inputs():
    input1 = 'x = 001;'
    input2 = 'x_2 = 0;'
    input3 = 'x = 0\ny = x;\nz = ---(x+y);'
    input4 = 'x = 1;\ny = 2;\nz = ---(x+y)*(x+-y);'

    print("\n\n")
    print("Input 1:\n" + input1)
    print("Output 1:")
    interpreter.interpret(input1)
    print("\n\n")

    print("Input 2:\n" + input2)
    print("Output 2:")
    interpreter.interpret(input2)
    print("\n\n")

    print("Input 3:\n" + input3)
    print("Output 3:")
    interpreter.interpret(input3)
    print("\n\n")

    print("Input 4:\n" + input4)
    print("Output 4:")
    interpreter.interpret(input4)



def process_file_input():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, 'r') as file:
            input_code = file.read()
            print(f"\nInput Code:\n{input_code}\n")
            interpreter.interpret(input_code)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# Prompt user for option
option = input("Enter 1 to process hardcoded inputs or 2 to provide a file name: ")

if option == '1':
    process_hardcoded_inputs()
elif option == '2':
    process_file_input()
else:
    print("Invalid option. Please try again.")


