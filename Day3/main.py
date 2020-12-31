def read_input():
    with open("Day3/input.txt", "r") as f:
        return f.readlines()

def part1():
    data = read_input()
    i = 1
    j = 3
    ans = 0
    while i < len(data):
        if data[i][j] == '#':
            ans += 1
        i = (i + 1)
        j = (j + 3) % 31
    return ans

def part2(s1, s2):
    data = read_input()
    i = s1
    j = s2
    ans = 0
    while i < len(data):
        if data[i][j] == '#':
            ans += 1
        i = (i + s1)
        j = (j + s2) % 31
    return ans



if __name__ == "__main__":
    print(f"Part1: {part1()}")
    p2 = part2(1, 1) * part2(1, 3) * part2(1, 5) * part2(1, 7) * part2(2, 1)
    print(f"Part1: {p2}")
