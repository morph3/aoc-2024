import re
with open("input.txt") as f:
    data = f.read().strip()


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

"""
ans = 0
for i in range(len(data)):
    #print(data[i])
    if data[i:i+4] == "mul(":
        # find where it closes
        idx = 4
        for j in range(4,20):
            if data[i+j] == ")":
                print(data[i:i+j+1])
                break
            if isinstance(data[i+j], int) or data[i+j] == ",":
                print(data[i+j])
                # if the char is not int or not , 
                # break
                break
            idx += 1

        #print(data[i:i+idx+1])
        #print(idx)
        ans += eval_mul(data[i:i+idx+1])
"""

regex = r"mul\((\d+),(\d+)\)"

matches = re.finditer(regex, data, re.MULTILINE)
ans = 0
for match in matches:
    #print(match.group(0))
    ans += eval_mul(match.group(0))

print(ans)
