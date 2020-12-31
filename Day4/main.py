def read_input():
    with open("Day4/input.txt", "r")as f:
        return f.readlines()

def parse_data():
    inp = read_input()
    data = [{} for x in range(500)]
    inp = read_input()
    k = 0
    for i in range(len(inp)):
        line = read_input()[i]
        if line == "\n":
            k = k + 1
            continue
        linef = line.split(" ", line.count(" "))
        for kv in linef:
            key = kv.split(':')[0]
            val = kv.split(':')[1].rstrip()
            data[k][key] = val
    return data


def part1():
    ans = 0
    reqs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    data = parse_data()
    for e in data:
        if all(req in e for req in reqs):
            ans = ans + 1

    return ans

def part2():
    ans = 0
    reqs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    ecl_reqs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    data = parse_data()
    for e in data:
        if all(req in e for req in reqs):
            if int(e['byr']) >= 1920 and int(e['byr']) <= 2002:
                if int(e['iyr']) >= 2010 and int(e['iyr']) <= 2020:
                    if check_height(e['hgt']):
                        if check_hcl(e['hcl']):
                            if int(e['eyr']) >= 2020 and int(e['eyr']) <= 2030:
                                if any(req in e['ecl'] for req in ecl_reqs):
                                    if len(e['pid']) == 9 and e['pid'].isdigit():
                                        ans = ans + 1

    return ans

    
def check_height(s):
    if 'cm' in s:
        return int(s[:-2]) >= 150 and int(s[:-2]) <= 193
    elif 'in' in s:
        return int(s[:-2]) >= 59 and int(s[:-2]) <= 76
    return False

def check_hcl(s):
    req1 = [str(i) for i in range(10)]
    req2 = ['a', 'b', 'c', 'd', 'e', 'f']
    reqs = req1 + req2
    ans = True
    if s[0] == '#' and len(s) == 7:
        for c in s[1:]:
            if reqs.count(c) == 0:
                ans = False
        return ans

    return False



if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")

