# Function to perform the calculation based on the operator
def calculate(num1, op, num2):
    if op == "+": return num1 + num2 
    elif op == "-": return num1 - num2
    elif op == "*": return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "error division by zero"
        return num1 / num2 
        

    # Use an if-elif-else chain to check the operator
    # If the operator is "+", return the sum of num1 and num2
    # If the operator is "-", return the difference between num1 and num2
    # If the operator is "*", return the product of num1 and num2
    # If the operator is "/", check if num2 is zero.
    # If num2 is zero, return an error message for division by zero.
    # Otherwise, return the result of the division.
    pass # Remove this line and add your code here

# This block of code will only run when the script is executed directly
if __name__ == "__main__":
        print("<======welcome to my Calculator App======>\n")
        while True:
             print("Operators: +,-,*,/ or exit")
             op = input("enter the operator:")

             if op == "exit":
                break
             if op not in "+,-,*/":
                  print("Invalid Operator")
                  continue
             
             num1 = float(input("Enter a First Number: "))
             num2 = float(input("Enter a Second number: "))

             result = calculate(num1 , op , num2)
             print(result)

    # 1. Print a welcome message for the user.
    #    Example: "===== Welcome to HERE AND NOW AI's Calculator App =====\n"

    # 2. Start an infinite loop to keep the calculator running.
    #    HINT: A 'while True:' loop is a good choice here.

        # 3. Inside the loop, first, inform the user about the available options.
        #    Print something like: "Operators: +, -, *, / or exit"

        # 4. Get input from the user for the desired operator.
        #    Store it in a variable, for example, 'op'.

        # 5. Add a condition to check if the user wants to 'exit'.
        #    If so, 'break' the loop.

        # 6. Check if the operator is valid (i.e., one of '+', '-', '*', '/').
        #    If not, print an error message and 'continue' to the next iteration.

        # 7. Get the first and second numbers from the user.
        #    Remember to convert them to a numeric type, like float.
        #    HINT: Use float(input(...))

        # 8. Call the 'calculate' function with the numbers and operator.
        #    Store the returned value in a 'result' variable.

        # 9. Print the final result to the user.
        #    Example format: f"Output: {result}"
        pass # Remove this line and implement the steps above.
