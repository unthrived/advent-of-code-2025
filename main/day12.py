from utils import read_txt

def create_grid(n, m):
    return [[0 for _ in range(n)] for _ in range(m)]

def transform(block, rotation, flip):
    """
    Applies transform to a block
    
    :param block: 3x3 blocks
    :param rotation: 0 no rotation, 1 90deg clock-wise, 2 180deg, 3 270
    :param flip: 0 no flip, 1 vertical flip
    """
    if flip:
        block[0], block[2] = block[2], block[0]
    if rotation == 1:
        block[0][0], block[0][2], block[2][2], block[2][0] = block[2][0], block[0][0], block[0][2], block[2][2]
        block[0][1], block[1][2], block[2][1], block[1][0] = block[1][0], block[0][1], block[1][2], block[2][1]
    if rotation == 2:
        block[0][0], block[0][2], block[2][2], block[2][0] = block[2][2], block[2][0], block[0][0], block[0][2]
        block[0][1], block[1][2], block[2][1], block[1][0] = block[2][1], block[1][0], block[0][1], block[1][2]
    if rotation == 3:
        block[0][0], block[0][2], block[2][2], block[2][0] = block[0][2], block[2][2], block[2][0], block[0][0]
        block[0][1], block[1][2], block[2][1], block[1][0] = block[1][2], block[2][1], block[1][0], block[0][1]
    return block

def fit_block_grid(grid, i, j, block):
    for k1 in range(3):
        for k2 in range(3):
            if grid[i+k1][j+k2] == 1 and block[0+k1][0+k2] == 1:
                return 0, grid
    for k1 in range(3):
        for k2 in range(3):
            grid[i+k1][j+k2] += block[0+k1][0+k2]
    return 1, grid

data = read_txt('data/day12.txt', numbers=False)
n = len(data)


blocks = dict()
grids = []
for i in range(n):
    if 'x' in data[i]:
        break
    if ':' in data[i]:
        blocks[int(data[i][0])] = [list(data[i+1]), list(data[i+2]), list(data[i+3])]

for value in blocks:
    for line in blocks[value]:
        for i in range(3):
            if line[i] == '#':
                line[i] = 1
            if line[i] == '.':
                line[i] = 0

for i in range(n):
    if 'x' in data[i]:
        data[i] = data[i].split(': ')
        data[i][0] = data[i][0].split('x')
        data[i][0] = list(map(int, data[i][0]))
        data[i][1] = data[i][1].split(' ')
        data[i][1] = list(map(int, data[i][1]))
        grids.append([data[i][0], data[i][1]])
print(blocks)
print(grids)
print('stock:', grids[0][1])

for i in range(2):
    for j in range(4):
        t = transform(blocks[0], j, i)
        for k in range(3):
            pass
        #print(t[k])
totalFit = 0
for i in range(len(grids)):
    grid = create_grid(grids[i][0][0], grids[i][0][1])
    stock = grids[i][1]
    #print(grid)
    #print(stock)
    totalStock = 0
    for i1 in range(len(stock)):
        for i2 in range(stock[i1]):
            block = blocks[i1]
            for j in range(len(grid)-2):
                for k in range(len(grid[0])-2):
                    for t1 in range(4):
                        for t2 in range(2):
                            t_block = transform(block, t1, t2)
                            fit, grid = fit_block_grid(grid, j, k, t_block)
                            if fit:
                                totalStock += 1
                                break
    print(i, totalStock, sum(stock))
    if totalStock >= sum(stock): totalFit += 1
    # for i in range(len(grid)): print(grid[i])
print(totalFit)