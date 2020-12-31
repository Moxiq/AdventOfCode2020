def read_input():
    with open("Day1/input.txt") as f:
        return [int(nbr) for nbr in f.readlines()]

def part1():
    data = read_input()
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]

def part2():
    data = read_input()
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            for k in range(j+1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]  


if __name__ == "__main__":
    print("Answer: " + str(part1()))
    print("Answer: " + str(part2()))
    


