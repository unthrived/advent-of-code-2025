from utils import read_txt

data = read_txt('data/day01.txt', numbers=False)

dial = 50
count = 0

for i, row in enumerate(data):
    if data[i][0] == 'R':
        dial = (dial + int(data[i][1:]))%100
    else:
        dial = (dial - int(data[i][1:]))%100
    if dial == 0: count += 1

print('p1',count)

dial = 50
count = 0

for i, row in enumerate(data):
    if data[i][0] == 'R':
        dial = dial + int(data[i][1:])
        while (dial > 99):
            dial = dial-100
            count += 1
    else:
        if dial == 0: count -= 1 # when the dial starts at 0 and goes left and ends at 0 we overcount it by one
        dial = dial - int(data[i][1:])
        while (dial < 0):
            dial = dial+100
            count += 1
        if dial == 0: count += 1
print('p2',count)
