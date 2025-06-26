def check_op(op):
    if op not in ('+', '-', '*', '/'):
        print("Please enter one of the operations")
        exit()

def check_nums(num):
    try:
        num = int(num)
    except:
        print("Please enter numbers only!")
        exit()

    if(num < 0):
        print("Please enter positive numbers")
        exit()

    return num

def do_op(num1, num2, op):
    print("Result:", num1, op, num2, "= ", end="")
    
    match op:
        case '+':
            res = num1 + num2
        case '-':
            res = num1 - num2
        case '*':
            res = num1 * num2
        case '/':
            if(num2 == 0):
                print("You can't divide by zero")
                exit()
            res = num1 / num2
        case _:
            print("Unkown operation")
            exit()
    print(res)
    
    return res

def save_logs(num1, num2, op, res):
    try:
        file = open("calculator_log.txt", "a", encoding="utf-8")
        data = f"Result: {num1} {op} {num2} = {res} \n"
        file.write(data)
        file.close()
    except FileNotFoundError:
        print("Something went wrong when creating the file")
        exit()

num1 = input("Enter the first number: ")
num1 = check_nums(num1)

num2 = input("Enter the second number: ")
num2 = check_nums(num2)

op = input("Enter an operation (+, -, *, /): ")
check_op(op)

res = do_op(num1, num2, op)

save_logs(num1, num2, op, res)

