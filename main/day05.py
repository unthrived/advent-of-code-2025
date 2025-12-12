from utils import read_txt

data = read_txt('data/day05.txt', numbers=False)
n = len(data)
for i in range(n):
    if data[i] == '':
        ids = data[i+1:]
        data = data[:i]
        break

for i in range(len(data)):
    data[i] = data[i].split('-')
count = 0
for k in range(len(ids)): 
    for i in range(len(data)):
        if int(ids[k]) in range(int(data[i][0]), int(data[i][1])+1):
            print(ids[k], data[i])
            count += 1
            break
print('p1', count)

for i in range(len(data)):
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])
for i in range(len(data)):
    for j in range(len(data)):
        if i!=j:
            if data[i][0] in range(data[j][0], data[j][1]):
                data[i][0] = data[j][1]
            if data[i][1] in range(data[j][0], data[j][1]):
                data[i][1] = data[j][0]
total = 0
active = [0 for i in range(len(data))]
for i in range(len(data)):
    if data[i][1] >= data[i][0]:
        active[i] = 1
print(active)
print(data)
changed = True
while changed:
    changed = False
    for i in range(len(data)):
        if active[i]:
            for j in range(len(data)):
                if active[j]:
                    if i != j:
                        if data[i][0] == data[j][1]:
                            data[i][0] = data[j][0]
                            active[j] = 0
                            changed = True
                        if data[i][1] == data[j][0]:
                            data[i][1] = data[j][1]
                            active[j] = 0
                            changed = True
total = 0
for i in range(len(active)):
    if active[i]:
        total += data[i][1] - data[i][0]
        total += 1
print(active)
print(data)
print(total)