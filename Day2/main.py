def read_input():
    with open("Day2/input.txt", "r") as f:
        return f.readlines()

def part1():
    counter = 0
    for line in read_input():
        min = int(line.split('-')[0])
        max = int(line.split('-')[1].split()[0])
        letter = line.split()[1].split(':'[0])[0]
        password = line.split(':')[1][1:]
        
        if password.count(letter) >= min and password.count(letter) <= max:
            counter += 1
    return counter

def part2():
    counter = 0
    for line in read_input():
        i = int(line.split('-')[0])
        j = int(line.split('-')[1].split()[0])
        letter = line.split()[1].split(':'[0])[0]
        password = line.split(':')[1][1:]

        if password[i-1] == letter and password[j-1] != letter:
            counter += 1
        elif password[j-1] == letter and password[i-1] != letter:
            counter += 1
    return counter


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")

