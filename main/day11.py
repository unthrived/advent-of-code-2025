from utils import read_txt
from functools import lru_cache
raw = read_txt('data/day11.txt', numbers=False)
n = len(raw)

from functools import lru_cache

def find_next(start, data, end):
    @lru_cache(None)
    def dfs(s):
        if end == 'out':
            if s == 'out':
                return 1
        else:
            if s == 'out':
                return 0
            if s == end:
                return 1
        total = 0
        for nxt in data[s]:
            total += dfs(nxt)
        return total
    return dfs(start)

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
    find_next('svr', data, 'fft')*
    find_next('fft', data, 'dac')*
    find_next('dac', data, 'out')
    )
print(
    # find_next('svr', data, 'dac'),
    # find_next('dac', data, 'fft'), # theres none going from dac to fft
    # find_next('fft', data, 'out')
    )
