def read_input():
    with open("Day5/input.txt", "r") as f:
        return f.readlines()

def part1():
    data = read_input()

    lowRow = 0
    highRow = 128

    lowCol = 0
    highCol = 8

    ids = []


    for line in data:
        for c in line:
            midRow = (highRow + lowRow) // 2
            midCol = (highCol + lowCol) // 2
            if c == 'F':
                highRow = midRow
            elif c == 'B':
                lowRow = midRow
            elif c == 'R':
                lowCol = midCol
            elif c == 'L':
                highCol = midCol
        
        ids.append(lowRow * 8 + lowCol)

        lowCol = lowRow = 0
        highCol = 8
        highRow = 128

    return max(ids)

def part2():
    data = read_input()

    lowRow = 0
    highRow = 128

    lowCol = 0
    highCol = 8

    ids = []


    for line in data:
        for c in line:
            midRow = (highRow + lowRow) // 2
            midCol = (highCol + lowCol) // 2
            if c == 'F':
                highRow = midRow
            elif c == 'B':
                lowRow = midRow
            elif c == 'R':
                lowCol = midCol
            elif c == 'L':
                highCol = midCol
        
        ids.append(lowRow * 8 + lowCol)

        lowCol = lowRow = 0
        highCol = 8
        highRow = 128

    ids.sort()
    for i in range(1, len(ids)-1):
        if ids[i+1] != ids[i]+1:
            return ids[i]+1
    

    

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")