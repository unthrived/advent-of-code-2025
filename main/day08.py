from utils import read_txt

def d2(pointA, pointB):
    return (pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2 + (pointA[2]-pointB[2])**2

data = read_txt('data/day08.txt', numbers=False)
n = len(data)
for i in range(n):
    data[i] = list(map(int,(data[i].split(','))))

pairs = []

for i in range(n-1):
    for j in range(i+1, n):
        dist = d2(data[i], data[j])
        pairs.append((dist, i, j))
pairs.sort(key=lambda x: x[0]) # sorting pairs is fine because we preserve i j
print(pairs[0])

s = [{}]
for k in range(20000):
    found_i = False
    found_j = False
    delete_j = False
    pop_j = None
    for i in range(len(s)):
        if pairs[k][1] in s[i]:
            found_i = i
        for j in range(len(s)):
            if pairs[k][2] in s[j]:
                found_j = j
        if found_i and found_j:
            if found_i!=found_j: # if both are found, we concat the sets
                s[found_i] |= s[found_j]
                delete_j = True
                pop_j = found_j
                break
        if found_i: 
            s[found_i] |= set([pairs[k][1], pairs[k][2]])
        if found_j:
            s[found_j] |= set([pairs[k][1], pairs[k][2]])
    if not found_i and not found_j:
        s.append(set([pairs[k][1], pairs[k][2]]))
    if delete_j: s.pop(pop_j)
    if len(s[1]) == n:
        print(data[pairs[k][1]], data[pairs[k][2]])
        print(data[pairs[k][1]][0] * data[pairs[k][2]][0])
        break
