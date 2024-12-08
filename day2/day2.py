import copy
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
        #print(f"line: {temp_arr} -> steps {steps}")
        return 0


def check_toleratable(arr):
    print(f"Original arr {arr}")
    # [54, 56, 54, 52, 51, 49]
    arr3 = copy.deepcopy(arr)
    arr4 = copy.deepcopy(arr)
    del arr3[0]
    del arr4[1]
    if ( check_safe(arr3) or check_safe(arr4)):
        print(f"tolerated with arr1 ?: {check_safe(arr3)}")
        print(f"tolerated with arr2 ?: {check_safe(arr4)}")
        return 1

    if arr[0] > arr[1]:
        # this is a decreasing arr
        for i in range(len(arr)):
            if abs(arr[i] - arr[i+1]) > 3:
                print(f"arr before deletion: {arr}")
                # the step is very high
                arr1 = copy.deepcopy(arr)
                arr2 = copy.deepcopy(arr)

                # if one of the arrays becomes safe we are good to go
                del arr1[i]
                del arr2[i+1]
                print(f"arr1 -> {arr1}")
                print(f"arr2 -> {arr2}")
                print(f"is arr1 safe? {check_safe(arr1)}")
                print(f"is arr2 safe? {check_safe(arr2)}")
                if ( check_safe(arr1) or check_safe(arr2)):
                    print(f"tolerated with arr1 ?: {check_safe(arr1)}")
                    print(f"tolerated with arr2 ?: {check_safe(arr2)}")
                    return 1
                else:
                    return 0

            if arr[i] < arr[i + 1 ]:
                # arr started increasing or equaled
                arr1 = copy.deepcopy(arr)
                arr2 = copy.deepcopy(arr)

                # if one of the arrays becomes safe we are good to go
                del arr1[i]
                del arr2[i+1]
                print(f"arr1 -> {arr1}")
                print(f"arr2 -> {arr2}")
                print(f"is arr1 safe? {check_safe(arr1)}")
                print(f"is arr2 safe? {check_safe(arr2)}")

                if ( check_safe(arr1) or check_safe(arr2)) :
                    print(f"tolerated with arr1 ?: {check_safe(arr1)}")
                    print(f"tolerated with arr2 ?: {check_safe(arr2)}")
                    return 1
                else:
                    return 0
            if arr[i] == arr[i+1]:
                del arr[i+1]
                if check_safe(arr):
                    print(f"tolerated with arr ?: {arr}")
                    return 1
                else:
                    return 0
    if arr[0] < arr[1]:
        # this is an increasing arr
        # not tolerated [14, 16, 18, 19, 21, 24, 22, 27]
        for i in range(len(arr)):
            if abs(arr[i] - arr[i+1]) > 3:
                # the step is very high
                # remove this element from the array and check one more time
                arr1 = copy.deepcopy(arr)
                arr2 = copy.deepcopy(arr)

                # if one of the arrays becomes safe we are good to go
                del arr1[i]
                del arr2[i+1]
                print(f"arr1 -> {arr1}")
                print(f"arr2 -> {arr2}")
                print(f"is arr1 safe? {check_safe(arr1)}")
                print(f"is arr2 safe? {check_safe(arr2)}")

                if ( check_safe(arr1) or check_safe(arr2)):

                    print(f"tolerated with arr1 ?: {check_safe(arr1)}")
                    print(f"tolerated with arr2 ?: {check_safe(arr2)}")

                    return 1
                else:
                    return 0

            if arr[i] > arr[i + 1 ]:
                # arr started decreasing
                arr1 = copy.deepcopy(arr)
                arr2 = copy.deepcopy(arr)

                # if one of the arrays becomes safe we are good to go
                del arr2[i+1]
                del arr1[i]
                if ( check_safe(arr1) or check_safe(arr2)) :
                    print(f"tolerated with arr1 ?: {check_safe(arr1)}")
                    print(f"tolerated with arr2 ?: {check_safe(arr2)}")
                    return 1
                else:
                    return 0
            if arr[i] == arr[i+1]:
                del arr[i+1]
                if check_safe(arr):
                    print(f"tolerated with arr ?: {check_safe(arr)}")
                    return 1
                else:
                    return 0

    if arr[0] == arr[1]:
        del arr[0]
        if check_safe(arr):
            return 1
        else:
            return 0


unsafes_arr = []


def check_can_tolerate(unsafes):
    toleratables = 0
    for arr in unsafes:
        if check_toleratable(arr):
            toleratables += 1
        else:
            print(f"\033[91m{arr}\033[0m")
    return toleratables

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
            unsafes_arr.append(temp_arr)
            unsafes += 1

    print(f"safes: {safes}")
    print(f"unsafes: {unsafes}")
    toleratables = check_can_tolerate(unsafes_arr)
    print(f"toleratables {toleratables}")
    # 538 too low.
    # 52 toleratable
    # 486 safes
    print(f"safes + toleratables {safes + toleratables}")

    print(check_can_tolerate([[48, 48, 46, 45, 44, 40, 41]]))