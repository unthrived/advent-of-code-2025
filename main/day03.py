from utils import read_txt

data = read_txt('data/day03.txt', numbers=False)
print(data)
n = len(data)
# brute force part 1
# total = 0
# for i in range(n):
#     m = len(data[i])
#     highest = int(data[i][0]+data[i][1])
#     for j in range(m):
#         for k in range(j+1,m):
#             current = int(data[i][j]+data[i][k])
#             # print(current)
#             if current > highest:
#                 highest = current
#     total += highest
# print(total)

thought_process = """
Essentially we want to find the highest value from all the numbers, except 12
then choose the leftmost highest, and then do the same for the queue minus one.
"""
def find_highest(string, queue):
    n = len(string)
    string = string[:n-queue+1]
    highest = 0
    for i in range(n-queue+1):
        if int(string[i]) > highest:
            highest = int(string[i])
            first_i = i
    return(first_i)
total = 0
for row in range(n):
    a = data[row] 
    result = ''
    for i in reversed(range(1,13)):
        index = find_highest(a, i)
        result += a[index]
        a = a[index+1:]
    total += int(result)
print(total)
