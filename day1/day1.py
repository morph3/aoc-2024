

with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
arr1 = []
arr2 = []
for line in lines:
    arr1.append(line.split("   ")[0])
    arr2.append(line.split("   ")[1])

arr1.sort(reverse=True)
arr2.sort(reverse=True)

distance = 0
for i in range(len(arr1)):
    arr1_popped = arr1.pop()
    arr2_popped = arr2.pop()
    distance += abs(int(arr1_popped) - int(arr2_popped))

print(distance)