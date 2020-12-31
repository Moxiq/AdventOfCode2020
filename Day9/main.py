def read_input():
    with open("Day9/input.txt") as f:
        return f.readlines()

def part1():
    data = read_input()

    # Convert to int list
    data = [int(i) for i in data]

    for i in range(len(data)):
        if not test_sum(data[i:i+25], data[i+25]):
            return data[i+25]

def part2():
    data = [int(i) for i in read_input()]

    p1 = part1()

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if sum(data[i:j+1]) == p1:
                return min(data[i:j+1]) + max(data[i:j+1])


def test_sum(nums, sum):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == sum:
                return True
    return False



if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
