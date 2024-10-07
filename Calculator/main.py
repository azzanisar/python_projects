def add(n1, n2):
    return n1 + n2

#Storing Functions as a Variable Value
add_operation = add

def subtract(n1,n2):
    return n1 - n2

subtract_operation = subtract

def multiply(n1, n2):
    return n1 * n2

multiply_operation = multiply

def divide(n1,n2):
    return n1 / n2

divide_operation = divide


operations = {
    "+" : add_operation,
    "-" : subtract_operation,
    "*" : multiply_operation,
    "/" : divide_operation,
}

#result = operations["*"](n1=5, n2= 3)
#print(result)
#print(operations["*"](n1=4, n2=8))

#Function to calculate all operations

def calculate(n1,n2,op):
    if op == "+":
        output = operations["+"](n1, n2)

    elif op == "-":
        output = operations["-"](n1, n2)

    elif op == "*":
        output = operations["*"](n1, n2)

    elif op == "/":
        output = operations["/"](n1, n2)

    else:
        raise ValueError("Invalid operator.")


    return output



from art import logo
print(logo)
#so we kept this user input outside while loop so that everytime we type yes to continue
#with previous calculation, it doesn't repeatedly overwrite this user input
first_num = float(input("What's the first number?: "))

#a list to keep track of all previous results as first number
number_list = []

continue_calculating = True
while continue_calculating:
    #for symbol in operations:
        #print(symbol) it prints all keys in operations dictionary
    operator = input("+" "\n" "-" "\n" "*" "\n" "/" "\n" "Pick an operation: ")
    next_num = float(input("What's the next number?: "))
    #answer= operations[operator](first_num,next_num)
    #print(f"{first_num} {operator} {next_num} = {answer}")

    number_list.append(first_num)
    print(number_list)
    result = calculate(n1=first_num,n2=next_num,op=operator)
    print(f"{first_num} {operator} {next_num} =", result)
    next_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if next_calculation == 'y':
        #program loops to use the previous result as the first num
        #so the while loop continues and asks for the operator and repeats calculation
       first_num = result


    elif next_calculation == 'n':
        #program will ask user for the first number again and
        #it wipes out all memory of previous calculations
        print(logo)
        first_num = float(input("What's the first number?: "))
        number_list=[]










