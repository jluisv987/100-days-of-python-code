def add(x,y):
    return x+y

def substrac(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

operations={
    "+":add,
    "-":substrac,
    "*":multiply,
    "/":divide
}
carry = 'no'
print("Simple calculator")
while True:
    if carry == 'no':
        num1 = int(input("Input the first number \n"))
    num2 = int(input("Input the second number \n"))
    symbol = input("What operation? '+','-','*','/'\n")
    function_c = operations[symbol]
    num1 = function_c(num1,num2)
    print(f"Calculator output: {num1}")
    exit = input("Exit? type 'yes' or 'no'\n")
    if exit == 'yes':
        break
    carry = input("Save the output for another operation? types 'yes' or 'no'\n")