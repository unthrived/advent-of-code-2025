from utils import read_txt
import math

def divisors(n):
    "there are more efficient ways ofc"
    div = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            div.append(i)
            if i != 1: div.append(int(n/i))
    return div

def create_pattern(digits, repetitions):
    """
    Essentially 303030 is divisible by 10101 because its 3 repetitions we get 3 1's
    the zeros in between 10101 determines the size of the number-1.
    So this function basically gives us the pattern number which we will use
    in order to divide the big number.
    """
    return int('1'+(('0'*(digits-1))+'1')*(repetitions-1)) # lol

data = read_txt('data/day02.txt', numbers=False)
data = data[0].split(',')
n = len(data)
total = 0
for i in range(n):
    data[i] = data[i].split('-')
for i in range(n):
    for j in range(int(data[i][0]), int(data[i][1])+1):
        l = len(str(j))
        div = divisors(l)[:]
        for i in range(len(div)):
            pattern = create_pattern(div[i], int(l/div[i]))
            if j%pattern == 0 and j>9:
                # print(j, pattern)
                total+=j
                break
            
print(total)

# bit ugly brute force solution for part 1

# data = read_txt('data/day02.txt', numbers=False)
# data = data[0].split(',')
# n = len(data)
# count = 0
# for i in range(n):
#     data[i] = data[i].split('-')
# for i in range(n):
#     for j in range(int(data[i][0]), int(data[i][1])+1):
#         s = str(j)
#         d = len(s)
#         if d%2 == 0 and s[0:int(d/2)] == s[int(d/2):d]:
#             count += j
# print(count) 

