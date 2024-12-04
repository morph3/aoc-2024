def check_safe(temp_arr):
    flag = 1 # 1 for safe, 0 for unsafe
    steps = []

    for i in range(len(temp_arr)-1):
        step = temp_arr[i] - temp_arr[i+1]
        steps.append(step)
    #print(f"line: {temp_arr} -> steps {steps}")
    pos_cnt = 0
    for step in steps:
        if abs(step) > 3:
            return 0
        if step == 0:
            return 0
        if step > 0:
            pos_cnt += 1
    if len(temp_arr) == pos_cnt+1:
        # all increasing
        return 1
    elif pos_cnt == 0:
        return 1
    else:
        print(f"line: {temp_arr} -> steps {steps}")
        return 0

def check_safe_tolerate(temp_arr):
    pass

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    # part1
    safes = 0
    unsafes = 0
    for line in lines:
        temp_arr = []
        [temp_arr.append(int(x)) for x in line.split(" ")]
        #print(temp_arr)
        res = check_safe(temp_arr)
        if res:
            safes += 1
        else:
            unsafes += 1

    print(f"safes: {safes}")
    print(f"unsafes: {unsafes}")
