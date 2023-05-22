# interpreter
# Interpreter for a programming language

A basic programming language interpreter is implemented in this project. Line by line, the interpreter examines input code from a text file. To tokenize the input code into intelligible chunks, it conducts lexical analysis. The code is then subjected to syntax analysis to see whether it adheres to programming language grammar norms. To store variable names and values, the interpreter keeps a symbol table. The code evaluates the expressions and assigns values to the variables if the syntax is correct. The variable names and corresponding values are then printed.


# The code has multiple conditions in order for the code to run

For example: 
input1 = 'x = 001;' this input will not work becaues two 0s came in the begining 
input3 = 'x = 0\ny = x;\nz = ---(x+y);' this will not work because each line should end with ; 

The code will be able to handle multiple signs followed by another sign and it should determine what to do with these signs
for example:

in input4 = 'x = 1;\ny = 2;\nz = ---(x+y)*(x+-y);' the --- in z should be proccessed as a - sign


# How the code run?

The code is designed to accept a file name to process. It also can show you how it will beperformhe task by processing the hardcoded inputs inside the code itself. 
The code is also designed to show you what exact line your file failed to follow the acceptable format so you know exactly what is wrong with your input.

# RUN 1

Enter 1 to process hardcoded inputs or 2 to provide a file name: 1



Input 1:
x = 001;
Output 1:
Error in line 1: x = 001;



Input 2:
x_2 = 0;
Output 2:
x_2 = 0



Input 3:
x = 0
y = x;
z = ---(x+y);
Output 3:
Error in line 1: x = 0



Input 4:
x = 1;
y = 2;
z = ---(x+y)*(x+-y);
Output 4:
x = 1
y = 2
z = 3

# RUN 2

Enter 1 to process hardcoded inputs or 2 to provide a file name: 2
Enter the file name: test1.txt

Input Code:
a = 10;
b = 5;
c = a + b;
x = 2;
y = x * x;
z = x + y - c;
div = 42;
br = div/2;
result = (x + y) * (z - br);


a = 10
b = 5
c = 15
x = 2
y = 4
z = -9
div = 42
br = 21.0
result = -180.0

# RUN 3

Enter 1 to process hardcoded inputs or 2 to provide a file name: 2
Enter the file name: test2.txt

Input Code:
a = 10;
b = 5;
c = a + b;
x = 2;
y = x * x;
z = x + y - c;
div = 42;
br = div/0;
result = (x + y) * (z - br);


Division by zero in line 8
Error in line 8: br = div/0;

Process finished with exit code 0
