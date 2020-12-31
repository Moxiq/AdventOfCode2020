def read_input():
    with open("Day6/input.txt", "r") as f:
        return f.readlines()

def part1():
    ans = 0
    duplicates = []
    for line in read_input():
        if line == '\n':
            duplicates.clear()
        for c in line:
            if c not in duplicates and c is not '\n':
                ans += 1
                duplicates.append(c)

    return ans

def part2():
    ans = 0
    isFirst = True
    duplicates = []
    for line in read_input():
        if line == '\n':
            isFirst = True
            ans += len(duplicates)
            duplicates.clear()
            continue
        else:
            if isFirst:
                for c in line:
                    if not c == '\n':
                        duplicates.append(c)
            else:
                for c in duplicates[:]:
                    if c not in line:
                        duplicates.remove(c)
        isFirst = False
      
    ans += len(duplicates)
    return ans

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")