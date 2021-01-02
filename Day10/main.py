def read_input():
    with open("Day10/input.txt") as f:
        return f.readlines()

def part1():
    data = [int(i) for i in read_input()]
    
    diffs = []
    order = []
    prev = 0

    while len(data) > 0:
        ad = min(data)
        diffs.append(ad - prev)
        data.remove(ad)
        prev = ad
    diffs.append(3)
    return diffs.count(1) * diffs.count(3)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")