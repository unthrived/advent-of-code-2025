def read_txt(path, numbers=True):
    data = []
    if numbers:
        with open(path, "r") as file:
            for line in file:
                numbers = list(map(int, line.split()))
                data.append(numbers)
    else: 
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                data.append(line)
    return data