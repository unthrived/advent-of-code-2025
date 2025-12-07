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

# part two not done yet
nodes = {}

for i in range(n-1):
    for j in range(m):
        if data[i][j] == '|':
            if data[i+1][j] == '^':
                nodes[i,j] = (i+1,j-1),(i+1,j+1)
            if data[i+1][j] == '|':
                nodes[i,j] = (i+1,j)
print(nodes)

def n_timeline(node, nodes):
    if node[0] == 14: return 1
    elif len(node) == 3: # split universe
        return n_timeline(nodes[node[1]], nodes) + n_timeline(nodes[node[2]], nodes)
    else:
        return n_timeline(nodes[node[1]], nodes)
    
print(n_timeline(((2, 6), (2, 8)), nodes))