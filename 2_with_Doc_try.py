'''
# OBJECTIVE
 - Use comments and documentation to make the code more intuitive and understandable
--
Comments/Documentation help programmers better understand the intent and functionality of the program
Types: Docstrings | Single-line comment | Multi-line comment
Docstrings are strings used right after the definition of a function, method, class, or module. They are used to document our code.
'''
# This is a single-line comment
'''
This is a multi-line comment
'''

class Calculator:
    def __init__(self, operand_1, operand_2):
        self.operand_1 = operand_1
        self.operand_2 = operand_2

    def calculate_sum(self):
        return self.operand_1 + self.operand_2
    
    def calculate_product(self):
        return self.operand_1 * self.operand_2

    def calculate_difference(self):
        return self.operand_1 - self.operand_2
    
    def calculate_quotient(self):
        return self.operand_1 / self.operand_2

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operands = Calculator(num_1, num_2)
choice = 1
while choice != 0:
    print("Enter Choice of Arithmetic Operation")
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice: "))
    print(f"Entered choice is: {choice}")
    if choice == 1:
        print("Result: ", operands.calculate_sum())
    elif choice == 2:
        print("Result: ", operands.calculate_difference())
    elif choice == 3:
        print("Result: ", operands.calculate_product())
    elif choice == 4:
        print("Result: ", round(operands.calculate_quotient(),2))
    elif choice == 0:
        print("Exiting!")
        print(f"Entered choice 0 to end program execution")
    else:
        print("Not a valid choice")


