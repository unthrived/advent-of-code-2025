from utils import read_txt

def d2(pointA, pointB):
    return (pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2 + (pointA[2]-pointB[2])**2

# very bad solution
data = read_txt('data/day08.txt', numbers=False)
n = len(data)
for i in range(n):
    data[i] = list(map(int,(data[i].split(','))))

chain = []
for k in range(1000):
    print(k)
    lowest = float('inf')
    lowest_i = None
    lowest_j = None
    for i in range(0, n-1):
        for j in range(i+1, n):
            if [i,j] not in chain:
                if d2(data[i], data[j]) < lowest:
                    lowest = d2(data[i], data[j])
                    print(lowest, i, j)
                    lowest_i = i
                    lowest_j = j
    chain.append([lowest_i, lowest_j])
print(chain)

values = [set(chain[0])]
for i in range(1, len(chain)):
    found = False
    for j in range(len(values)):
        if chain[i][0] in values[j] or chain[i][1] in values[j]:
            print(chain[i][0], values[j])
            values[j] |= set(chain[i])
            found = True
            break
    if not found:
        values.append(set(chain[i]))
print(values)

prev = []
while prev != values:
    prev == values[:]
    for i in range(len(values)-1):
        for j in range(i+1, len(values)):
            if values[i] & values[j]:
                values[i] |= values[j]
                values.pop(j)
                break
# print(values)

for i in range(len(values)):
    print(len(values[i]))
