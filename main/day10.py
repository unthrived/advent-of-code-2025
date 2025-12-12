from utils import read_txt
from math import floor
import re

def swap(string, pos):
    # string = list(string)
    if string[pos] == '#':
        string = string[:pos]+'.'+string[pos+1:]
    else:
        string = string[:pos]+'#'+string[pos+1:]
    return string

def add(l, pos, amount):
    l[pos] = l[pos] + amount
    return l

def check_off(string):
    off = True
    for i in range(len(string)):
        if string[i] == '#':
            off = False
            return off
    return off

def create_permutations(size):
    "binary permutations"
    perms = []
    for i in range(2**size):
        aux = re.sub('0b','',bin(i))
        binary = [0]*(size-len(aux))
        for j in range(len(aux)):
            binary.append(int(aux[j]))
        perms.append(binary)
    return perms

def create_sub_permutations(l, size):
    "exact sum permutations in list of sizes to sum up to big size"
    if len(l) == 0: 
        if size == 0:
            return [[]]
        return []
    perms = []
    div = floor(size / l[0])
    for i in (range(div+1)):
        # print(create_sub_permutations(l[1:], size-i*l[0]), 'hi', l, size)
        subterms = create_sub_permutations(l[1:], size-i*l[0])
        for p in subterms:
            perms.append([i]+p)
    return perms

data = read_txt('data/day10.txt', numbers=False)

n = len(data)
for i in range(n):
    data[i] = data[i].split(' ')
for i in range(n):
    data[i][0] = re.sub(r'[\[\]]','',data[i][0])
    for j in range(1, len(data[i])-1):
        data[i][j] = re.sub(r'[\(\)]','',data[i][j])
        data[i][j] = data[i][j].split(',')
        data[i][j] = list(map(int, data[i][j]))
    data[i][-1] = re.sub(r'[\{\}]', '', data[i][-1])
    data[i][-1] = data[i][-1].split(',')
    data[i][-1] = list(map(int, data[i][-1]))

p1=False
if p1:
    total = 0
    for i in range(n):
        lowest = float('inf')
        n_perms = len(data[i])-2
        perms = create_permutations(n_perms)
        for perm in perms:
            pattern = data[i][0]
            for j in range(len(perm)):
                if perm[j]:
                    # print(perm, data[i][j+1])
                    for k in range(len(data[i][j+1])):
                        pattern = swap(pattern, int(data[i][j+1][k]))
            # print(check_off(pattern), pattern)
            if check_off(pattern):
                count = 0
                for j in range(len(perm)):
                    count += perm[j]
                if count < lowest: lowest = count
        total += lowest
    print('p1', total)

p2=False
if p2:
    total = 0
    for i in range(n):
        lowest = float('inf')
        m = len(data[i])
        lengths = list(map(len, data[i][1:m-1]))
        size = sum(data[i][m-1])
        print(i)
        perms = create_sub_permutations(lengths, size)
        print(perms)
        for perm in perms:
            pattern = data[i][-1]
            initial = [0]*len(pattern)
            for j in range(len(perm)):
                if perm[j]:
                    for k in range(len(data[i][j+1])):
                        initial = add(initial, int(data[i][j+1][k]), perm[j])
                        # pattern = swap(pattern, int(data[i][j+1][k]))
            if initial == pattern:
                print(perm, pattern)
                count = 0
                for j in range(len(perm)):
                    count += perm[j]
                if count < lowest: lowest = count
            # print(check_off(pattern), pattern)
            # if check_off(pattern):
            #     count = 0
            #     for j in range(len(perm)):
            #         count += perm[j]
            #     if count < lowest: lowest = count
        total += lowest
        print(lowest)
    print('p2', total)

for i in range(n):
    print(data[i])

import numpy as np

for i in range(n):
    cols = len(data[i][-1])
    b = np.array(data[i][-1])
    A = np.zeros((len(data[i])-2, len(data[i][-1])))
    x = np.zeros(len(data[i])-2)
    x[0] = 0
    for j in range(len(data[i])-2):
        row = np.zeros(cols)
        for k in range(len(data[i][j+1])):
            row[data[i][j+1][k]] = 1
        #print(row)
        A[j] = row
    # print(A, A.shape)
    # print(x)
    # print(b)
    # print(x.dot(A))
    # 
"""
Gave up
Theres so much lin alg going on i didnt even do this in my maths bachelors :)
"""