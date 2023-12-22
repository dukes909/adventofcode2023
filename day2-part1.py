import re

sum = 0

matches = []
rlist = []
rglist = []
rgblist = []

rpattern = r"(\d+)(?= red)"
gpattern = r"(\d+)(?= green)"
bpattern = r"(\d+)(?= blue)"
idpattern = r"^Game\s\d+"

with open('/home/opalko/Desktop/Python Projects/Advent of Code 2023/day 2/day2-part1-data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
            
        has_match = False
        for match in re.finditer(rpattern, line):
            value = int(match.group(0).split()[0])
            if value > 12:
                has_match = True
                break
        if not has_match:
            rlist.append(line)
    for line in rlist:
        has_match = False
        for match in re.finditer(gpattern, line):
            value = int(match.group(0).split()[0])
            if value > 13:
                has_match = True
                break
        if not has_match:
            rglist.append(line)
    for line in rglist:
        has_match = False
        for match in re.finditer(bpattern, line):
            value = int(match.group(0).split()[0])
            if value > 14:
                has_match = True
                break
        if not has_match:
            rgblist.append(line)    
    for line in rgblist:
        match = re.search(idpattern, line)
        value = int(match.group(0).split()[1])
        sum += value
    print(sum)

