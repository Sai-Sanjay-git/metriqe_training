def calculate (num1 , op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "error division by zero"
        return num1 / num2
    

if __name__ == "__main__":
    print("<====welcome to my calculator====>\n")

    while True:
        print("operators: +,-,*,/ or exit")
        op = input("Enter the operator: ")

        if op == "exit":
            break

        if op not in " +,-,*,/":
            print("Invalid operator")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the first number: "))

        result = calculate (num1 , op , num2)
        print (result)