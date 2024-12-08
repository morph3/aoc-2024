from itertools import product


def eval_expr(operations, numbers):
    numbers = numbers.split(" ")
    equation = ""
    for i in range(len(numbers)):
        equation += numbers[i]
        if i < len(numbers) - 1:  # Add an operator between numbers
            equation += operations[i % len(operations)]
    
    numbers = [int(x) for x in numbers]
    result = numbers[0]
    for i in range(len(operations)):
        operator = operations[i]
        next_num = numbers[i+1]
        if operator == '+':
            result += next_num
        elif operator == '*':
            result *= next_num
        elif operator == "|":
            result = int(str(result)+str(next_num))
    return equation, result


def generate_operation_list(available_ops, total_ops):
    return list(product(available_ops,repeat=total_ops))

def satisfy_eq(result, numbers, available_ops):
    tokens = numbers.split(" ")
    op_list = generate_operation_list(available_ops, len(tokens)-1)
    equations = []
    #print(tokens)
    eqn = ""
    for operations in op_list:
            equation, curr_res = eval_expr(operations,numbers)
            #print(f"Equation: {equation}")
            #print(f"curr_res: {curr_res}")
            if curr_res == int(result):
                print(equation, result)
                return 1
    return 0

def part1(data):
    sat = 0
    total_sum = 0
    for line in data:
        result = int(line.split(":")[0])
        equation = line.split(":")[1].strip()
        #print(equation)
        if satisfy_eq(result, equation, "+*"):
            sat += 1
            total_sum += result
    print(sat)
    print(total_sum)
    return



def part2(data):
    sat = 0
    total_sum = 0
    for line in data:
        result = int(line.split(":")[0])
        equation = line.split(":")[1].strip()
        #print(equation)
        if satisfy_eq(result, equation, "+*|"):
            sat += 1
            total_sum += result
    print(sat)
    print(total_sum)
    return



if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    #part1(data)
    part2(data)

