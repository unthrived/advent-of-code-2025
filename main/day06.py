from utils import read_txt

#p1
data = read_txt('data/day06.txt', numbers=False)
for i in range(len(data)):
    data[i] = data[i].split()
n = len(data)
m = len(data[0])
total_2 = 0
for k in range(m):
    if data[n-1][k] == '+':
        total = 0
        for i in range(n-1):
            total += int(data[i][k])
        total_2 += total
    else:
        product = 1
        for i in range(n-1):
            product *= int(data[i][k])
        total_2 += product
print('p1', total_2)

#p2 redo cause splitlines better than split here
with open('data/day06.txt', "r") as file:
    data = file.read().splitlines()
n = len(data)
m = len(data[0])
col = 0
sign = [j for j in range(m) if data[n-1][j] in '+*']
sign.append(m+1) # added a fake last sign so you know where to stop on the prev
total_2 = 0
for k in range(len(sign)-1):
    total = 0
    product = 1
    for j in range(sign[k], sign[k+1]-1):
        col = ''
        for i in range(n-1):
            col += data[i][j]
        if data[n-1][sign[k]] == '+':
            total += int(col)
        if data[n-1][sign[k]] == '*':
            product *= int(col)
    if total:
        total_2 += total
    else:
        total_2 += product
print('p2',total_2)