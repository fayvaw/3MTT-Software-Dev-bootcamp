'''
Created by Favour
Date: 07-09-2024
3MTT Software Dev Cohort2
FE/23/70949494
'''
def add_num(num1, num2):
    return num1 + num2

def subt_num(num1, num2):
    return num1 - num2

def prod_num(num1, num2):
    return num1 * num2

def quot_num(num1, num2):
    return num1/num2

def get_num():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    return num1, num2

def get_op():
    op = ''
    while not op in ("+", "-", "*", "/"):
        op = input("Enter an arithmetic operator (+, -, *, /): ")
        if op in ("+", "-", "*", "/"):
            break
        print("Please enter a valid operation!")
    return op

def main():
    num1, num2 = get_num()
    op = get_op()
    match op:
        case '+':
            result = add_num(num1, num2)
        case '-':
            result = subt_num(num1, num2)
        case '*':
            result = prod_num(num1, num2)
        case '/':
            result = quot_num(num1, num2)

    print(f"{num1} {op} {num2} = {result}")


if __name__ == '__main__':
    main()