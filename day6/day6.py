direction = {
    0:"north",
    1:"east",
    2:"south",
    3:"west"
}

def find_agent(data):
    i = 0
    j = 0
    for row in data:
        j = 0
        i += 1
        for col in row:
            j += 1
            if col == "^":
                return j-1,i-1

def display_board(data):
    for row in data:
        for col in row:
            if col == "X":
                print("\033[92mX\033[0m", end="")
            else:
                print(col, end="")
        print()

def mark_visited(data, x, y):
    #print(x, y)
    row = list(data[y])
    row[x] = "X"
    data[y] = ''.join(row)
    return data

def count_visited(data):
    score = 0
    for row in data:
        for col in row:
            if col == "X":
                score +=1
    return score

def part1(data):
    x, y = find_agent(data)
    mark_visited(data,x,y)
    print(f"Agent at coords {x}, {y}")
    k = 0
    curr_direction = direction[k%4]
    print(f"Current direction {curr_direction}")
    #display_board(data)
    while True:
        
        if False:
            input(">")
            display_board(data)
            print(f"coords: {x}, {y}")

        if curr_direction == "north":
            y += -1
        if curr_direction == "east":
            x += 1
        if curr_direction == "west":
            x += -1
        if curr_direction == "south":
            y += 1
        try:
            if data[y][x] == "#": # agent at position #
                k += 1
                if curr_direction == "north":
                    y += 1 # go one step back
                if curr_direction == "east":
                    x += -1
                if curr_direction == "west":
                    x += 1
                if curr_direction == "south":
                    y += -1
                curr_direction = direction[k%4]
        except:
            score = count_visited(data)
            display_board(data)
            print(f"visited cells: {score}")
            break
        data = mark_visited(data,x,y)

        

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    part1(data)