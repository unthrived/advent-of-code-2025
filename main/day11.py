from utils import read_txt
raw = read_txt('data/day11.txt', numbers=False)
n = len(raw)

def find_next(s, data, end):
    # print(s)
    if end == 'out':
        if s == 'out': return 1
    else:
        if s == 'out': return 0
        if s == end: return 1
    total = 0
    for i in range(len(data[s])):
        total += find_next(data[s][i], data, end)
        if data[s][i] in data['dac']:
            print(data[s][i], total)
    return total


for i in range(n):
    raw[i] = raw[i].split(': ')
for i in range(n):
    raw[i][1] = raw[i][1].split(' ')
data = dict()
for i in range(n):
    data[raw[i][0]] = raw[i][1]

# print(find_next('fft', data, 'out'))

# svr fft dac out
print(
    #find_next('svr', data, 'fft'),
    #find_next('fft', data, 'dac'), 
    find_next('dac', data, 'out')
    )

print(
    # find_next('svr', data, 'dac'),
    # find_next('dac', data, 'fft'), # theres none going from dac to fft
    # find_next('fft', data, 'out')
    )
