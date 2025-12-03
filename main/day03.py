from utils import read_txt

data = read_txt('data/day03.txt', numbers=False)
# print(data)
n = len(data)

thought_process = """
Essentially we want to find the highest value from all the numbers, except 12
then choose the leftmost highest, and then do the same for the queue minus one.
"""
def find_highest(string, queue):
    n = len(string)
    string = string[:n-queue+1] # +1 here is important to check one more because the queue is one less
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
    for i in reversed(range(1,13)): # part a is changing 13 for 3
        index = find_highest(a, i)
        result += a[index]
        a = a[index+1:]
    total += int(result)
print(total)