from utils import read_txt
data = read_txt('data/day12.txt', numbers=False)
n = len(data)
for i in range(n):
    print(data[i])

count = 0
for i in range(n):
    if 'x' in data[i]:
        break
    if ':' in data[i]:
        count += 1
    
print(count)
blocks = [[None]*count]
print(blocks)
for i in range(n):
    count = 0
    if 'x' in data[i]:
        break 
    if ':' in data[i]:
        blocks[count].extend([data[i+1], data[i+2], data[i+3]])
        count+=1
print(blocks)