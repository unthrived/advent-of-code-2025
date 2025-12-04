from utils import read_txt
import math

data = read_txt('data/day04.txt', numbers=False)
print(data)
n = len(data)
m = len(data[0])
print(n, m)
pad = [[0 for i in range(n+2)] for j in range(m+2)]
for i in range(n):
    for j in range(m):
        pad[i+1][j+1] = data[i][j]

directions = {}
for angle in range(0, 360, 45): 
    directions[angle] = [round(math.sin(math.pi*angle/180)), round(math.cos(math.pi*angle/180))]

total = 0
for i in range(1, n+2):
    for j in range(1, n+2):
        if pad[i][j] == '@':
            count = 0
            for angle in range(0, 360, 45):
                dx = directions[angle][0]
                dy = directions[angle][1]
                if pad[i+dx][j+dy] == '@': count += 1
            if count < 4:
                total += 1
print('p1', total)

total = 0
prev_total = -1
while total != prev_total:
    prev_total = total
    for i in range(1, n+2):
        for j in range(1, n+2):
            if pad[i][j] == '@':
                count = 0
                for angle in range(0, 360, 45):
                    dx = directions[angle][0]
                    dy = directions[angle][1]
                    if pad[i+dx][j+dy] == '@': count += 1
                if count < 4:
                    total += 1
                    pad[i][j] = 'x'
                    # print(i, j)
    # print(total, prev_total)
print('p2', total)