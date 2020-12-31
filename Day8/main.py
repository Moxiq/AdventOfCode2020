def run(data):
    t = 0
    acc = 0
    i = 0

    while i < len(data) and t < 1000:
        line = data[i]
        key, val = line.split()

        if key == 'acc':
            acc += int(val)
        
        elif key == 'jmp':
            i += int(val)
            t += 1
            continue

        t += 1
        i += 1

        if i >= len(data):
            return acc

    return -1


def read_input():
    with open("Day8/input.txt") as f:
        return f.readlines()

def part1():
    data = read_input()

    acc = 0
    executed = []

    i = 0

    while i not in executed:
        line = data[i]
        key, val = line.split()

        executed.append(i)

        if key == 'acc':
            acc += int(val)
        
        elif key == 'jmp':
            i += int(val)
            continue

        i += 1


    return acc


def part2():
    og_data = read_input()
    data = og_data.copy()

    for i in range(len(data)):
        key, val = data[i].split()
        if key == 'jmp':
            data[i] = 'nop ' + val
        elif key == 'nop':
            data[i] = 'jmp ' + val

        else:
            continue

        acc = 0
        i = 0
        t = 0

        while t < 1000:
            line = data[i]
            key, val = line.split()

            if key == 'acc':
                acc += int(val)
            
            elif key == 'jmp':
                i += int(val)
                t += 1
                if i == len(data):
                    return acc
                continue

            i += 1
            t += 1

            if i == len(data):
                return acc

        data = og_data.copy()


        



if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")