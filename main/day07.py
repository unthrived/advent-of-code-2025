from utils import read_txt

data = read_txt('data/day07.txt', numbers=False)
n = len(data)
m = len(data[0])
for i in range(n):
    data[i] = list(data[i])

count = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 'S':
            data[i+1][j] = '|'
        if data[i][j] == '^':
            if data[i-1][j] == '|':
                data[i][j+1] = '|'
                data[i][j-1] = '|'
                count += 1
        if data[i][j] == '.' and i > 0:
            if data[i-1][j] == '|':
                data[i][j] = '|'

# part 2
# recursion takes forever, solution was just summing bottom up
for j in range(m):
    if data[n-1][j] == '|': 
        data[n-1][j] = 1

for i in reversed(range(n-1)):
    for j in range(m):
        if data[i][j] == '|':
            if data[i+1][j] == '^':
                data[i][j] = data[i+1][j-1] + data[i+1][j+1]
            elif data[i+1][j] == '.':
                pass
            else:
                data[i][j] = data[i+1][j]

print(data[1])
     