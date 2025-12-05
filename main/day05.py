from utils import read_txt

data = read_txt('data/day05.txt', numbers=False)
print(data)
n = len(data)
for i in range(n):
    if data[i] == '':
        ids = data[i+1:]
        data = data[:i]
        break

for i in range(len(data)):
    data[i] = data[i].split('-')
print(data)
count = 0
for k in range(len(ids)): 
    for i in range(len(data)):
        if int(ids[k]) in range(int(data[i][0]), int(data[i][1])+1):
            print(ids[k], data[i])
            count += 1
            break
print('p1', count)

print(data)
for i in range(len(data)):
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])
final = [data[0]]
print(final)
for i in range(1, len(data)):
    print('###', data[i], final)
    found_left = False
    found_right = False
    for j in range(len(final)):
        found_left = False
        found_right = False
        if data[i][0] in range(final[j][0], final[j][1]+1):
            found_left = True
            print('left', final, data[i])
            for k in range(len(final)):
                if data[i][1] in range(final[k][0], final[k][1]+1):
                    print('right', k)
                    found_right = True
                    if j != k:
                        final[j][1] = final[k][1]
                        final[k][0] = -1
                        final[k][1] = 0
                        break
                if not found_right:
                    final[j][1] = data[i][1]
        elif data[i][1] in range(final[j][0], final[j][1]+1):
            found_right = True
            print('right',final, data[i])
            for k in range(len(final)):
                if data[i][0] in range(final[k][0], final[k][1]+1):
                    found_left = True
                    final[j][0] = data[k][0]
                    final[k][0] = -1
                    final[k][1] = 0
                if not found_left:
                    final[j][0] = data[i][0]
    if not found_right and not found_left:
        final.append(data[i])
print(final)