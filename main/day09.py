from utils import read_txt

def area(A, B):
    return (abs(A[0] - B[0])+1) * (abs(A[1] - B[1])+1)
def red_inside(A, B, C):
    x1 = min(A[0], B[0])
    x2 = min(A[1], B[1])
    y1 = max(A[0], B[0])
    y2 = max(A[1], B[1])
    if x1 < C[0] < y1:
        if x2 < C[1] < y2:
            return True
    return False

data = read_txt('data/day09.txt', numbers=False)

n = len(data)
for i in range(n): 
    data[i] = data[i].split(',')
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])

highest = 0
for i in range(n-1):
    for j in range(i+1, n):
        if area(data[i], data[j]) > highest: highest = area(data[i], data[j])
        print(i, j, area(data[i], data[j]))
print(highest)

# p2 # TOOK 3 HOURS TO RUN :) could be optimized but busy these days
green = []
for i in range(n-1):
    if i%2 == 0:
        print(data[i], range(data[i][0], data[i+1][0]))
        for k in range(min(data[i][0], data[i+1][0]), max(data[i][0], data[i+1][0])):
            green.append([k, data[i][1]])
    if i%2 == 1:
        print(data[i], range(data[i][1], data[i+1][1]))
        for k in range(min(data[i][1], data[i+1][1]), max(data[i][1], data[i+1][1])):
            green.append([data[i][0], k])
print(green)

highest = 0
for i in range(n-1):
    for j in range(i+1, n):
        print(i, n, j, n)
        red = False
        for k in range(len(green)):
            # print(data[i], data[j], green[k], red_inside(data[i], data[j], green[k]))
            if red_inside(data[i], data[j], green[k]):
                red = True
                break
        if not red:
            if area(data[i], data[j]) > highest: 
                highest = area(data[i], data[j])
                print(i, j, data[i], data[j], area(data[i], data[j]))
print(highest)

        # if area(data[i], data[j]) > highest: highest = area(data[i], data[j])