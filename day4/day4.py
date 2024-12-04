# horizontal, vertical, diagonal, written backwards

with open("input.txt") as f:
    data = f.read().strip()

import re

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def backwards(data):
    regex = r"SAMX"
    matches = re.finditer(regex, data, re.MULTILINE)
    cnt = 0
    for match in matches:
        cnt += 1
    return cnt

def horizontal(data):
    regex = r"XMAS"
    matches = re.finditer(regex, data, re.MULTILINE)
    cnt = 0
    for match in matches:
        cnt += 1
    return cnt


def diagonal(data):
    matrix1 = []
    matrix2 = []
    data = data.split("\n")

    for i,j in zip(reversed(range(len(data))), range(len(data))) :
        
        line = ("*"*i + data[j] ) + j*"*"
        matrix1.append(line)

    for i,j in zip(range(len(data)), reversed(range(len(data)))) :
        
        line = ("*"*i + data[i] ) + j*"*"
        matrix2.append(line)
    
    matrix1 = "\n".join(matrix1)
    matrix2 = "\n".join(matrix2)

    print(matrix1)
    print(matrix2)


    #h1 = horizontal(matrix1)
    #b1 = backwards(matrix1)
    v1 = vertical(matrix1)

    #h2 = horizontal(matrix2)
    #b2 = backwards(matrix2)
    v2 = vertical(matrix2)

    #return h1 + b1 + v1 + b2 + h2 + v2
    return v1+v2


def vertical(data):
    matrix = data.split("\n")
    matrix = transpose(matrix)
    # join each row
    for i in range(len(matrix)):
        matrix[i] = "".join(matrix[i])
    matrix = "\n".join(matrix)
    h = horizontal(matrix)
    b = backwards(matrix)
    print("Vertical")
    print(f"\t->horizontal {h}")
    print(f"\t->backwards {b}")
    return h+b


if __name__ ==  "__main__":
    
    # part1 
    with open("input.txt") as f:
        data = f.read().strip()

    ans = 0
    b = backwards(data)
    h = horizontal(data)
    v = vertical(data)
    d = diagonal(data)
    print(f"horizontal: {h}")
    print(f"vertical: {v}")
    print(f"diagonal: {d}")
    print(f"backwards: {b}")
    
    ans = b + h + v + d
    print(ans)

    # part2
