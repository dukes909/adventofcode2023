import re

sum = 0

matches = []
rlist = []
glist = []
blist = []
newlist = []

rpattern = r"(\d+)(?= red)"
gpattern = r"(\d+)(?= green)"
bpattern = r"(\d+)(?= blue)"
idpattern = r"^Game\s\d+"

with open('/home/opalko/Desktop/Python Projects/Advent of Code 2023/day 2/day2-part1-data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        print(f"line: {line}")
        rlist = []
        glist = []
        blist = []    
        has_match = False
        for match in re.finditer(rpattern, line):
            value = 0
            value = int(match.group(0).split()[0])
            rlist.append(value)
            print(f"red list at: {rlist}")
            rmax = max(rlist)
        for match in re.finditer(gpattern, line):
            value = 0
            value = int(match.group(0).split()[0])
            glist.append(value)
            print(f"green list at: {glist}")
            gmax = max(glist)
        for match in re.finditer(bpattern, line):
            value = 0
            value = int(match.group(0).split()[0])
            blist.append(value) 
            print(f"blue list at: {blist}")
            bmax = max(blist)
        print(f"max values: {rmax} {gmax} {bmax}")
        product = rmax * gmax * bmax
        sum += product
        newlist.append(product)   
    
    print(sum)

