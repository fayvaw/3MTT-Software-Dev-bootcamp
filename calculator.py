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

def get_num():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    return num1, num2

def main():
    num1, num2 = get_num()
    added = add_num(num1, num2)
    subtr = subt_num(num1, num2)
    prod = prod_num(num1, num2)

    print(f"Sum: {added}")
    print(f"Diff: {subtr}")
    print(f"Prod: {prod}")

if __name__ == '__main__':
    main()