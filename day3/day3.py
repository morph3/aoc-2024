import re


def eval_mul(a):
    if not a.startswith("mul"):
        return 0
    if not a.endswith(")"):
        return 0
    a = a.replace("mul(", "")
    a = a.replace(")", "")
    num1, num2 = a.split(",")
    
    #print(a)
    return int(num1) * int(num2)


def part1(data):
    ans = 0
    part1_regex = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(part1_regex, data, re.MULTILINE)

    for match in matches:
        #print(match.group(0))
        ans += (eval_mul(match.group(0)))
    return ans

def part2(data):
    part2_regex = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"
    matches = re.finditer(part2_regex, data, re.MULTILINE)
    
    do = True
    ans = 0

    for match in matches:
        if match.group(0) == "do()":
            do = True
        if match.group(0) == "don't()":
            do = False
        if do:
            ans += (eval_mul(match.group(0)))

    return ans


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()

    print(part1(data))
    print(part2(data))