# Don't panic! 
# It's just a program
# AOC 2023 Day 5 Part 2

import re
import sys
import time

seeds = []  # Standalone lists for each category
soil_map = [] 
fertilizer_map = []
water_map = []
light_map = []
temperature_map = []
humidity_map = []
location_map = []

temp_list = []
soil_list = []
fertilizer_list = []
water_list = []
light_list = []
temperature_list = []
humidity_list = []
location_list = []

equivalent_list = []

map_categories = ['location_map', 'humidity_map', 'temperature_map', 'light_map', 'water_map', 'fertilizer_map', 'soil_map']
map_dict = {}  # Create a dictionary to store the lists

seeds_regexp = re.compile(r"seeds:")

with open('/home/opalko/Desktop/Python Projects/Advent of Code 2023/day5/day5-data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    lines = [i for a, i in enumerate(lines) if i != '']
#    print(lines)

for line in lines:
    seeds_r = re.split(seeds_regexp, line)
    if len(seeds_r) > 1:  # Check if the split produced at least two elements
        seeds.extend(seeds_r[1].split())
for i in range(0, len(seeds)):
    seeds[i] = int(seeds[i])    
print(f"seeds to int {seeds}")    
    
number_lists = []  # Store the standalone lists using a counter
current_list = []  # Temporary list for each map section
map_started = False  # Flag to track map section start

for line in lines:
    if line.endswith("map:"):
        if current_list and map_started:  # Append previous list (excluding seed line)
            number_lists.append(current_list)
        current_list = []
        map_started = True  # Indicate map section start
    elif not line.endswith("map:"):
        if map_started:
            current_list.append(line)

# Handle the last list
if current_list and map_started:
    number_lists.append(current_list)

# Assign each standalone list to its own variable
soil_map = number_lists[0] 
fertilizer_map = number_lists[1]
water_map = number_lists[2]
light_map = number_lists[3]
temperature_map = number_lists[4]
humidity_map = number_lists[5]
location_map = number_lists[6]
print("Don't panic!")

# Process raw strings from the data file to create number_lists
for map_type in map_categories:
    number_lists = []  
    for map in eval(map_type):
        numbers = [int(number) for number in map.split()]  # Split and convert
        number_lists.append(numbers)  # Append the list of integers
    map_dict[map_type] = number_lists  # Assign to the dictionary

a_seed = False
x = 0 
while not a_seed:
    x += 1
 #   print(f"x = {x}")
 #   time.sleep(1)
    
    for el in map_dict['location_map']:
        newval = x
#        print(f"testing {newval} location map")
        lower_limit = el[0]
        upper_limit = lower_limit + el[2] - 1
        if newval >= lower_limit and newval <= upper_limit: 
 #           print(f"location_map testval: {newval} in range of {lower_limit} - {upper_limit}")
            if lower_limit < el[1]:
                newval = newval + (el[1] - lower_limit)
            else:
                newval = newval - (lower_limit - el[1])
 #           print(f"mapped to: {newval}")
            break
        else:
            continue

    for el in map_dict['humidity_map']:
 #       print(f"testing {newval} humidity map")
 #       print(f"element: {el}")
        lower_limit = el[0]
        upper_limit = lower_limit + el[2] - 1
        if newval >= lower_limit and newval <= upper_limit: 
 #           print(f"humidity testval: {newval} in range of {lower_limit} - {upper_limit}")
            if lower_limit < el[1]:
                newval = newval + (el[1] - lower_limit)
            else:
                newval = newval - (lower_limit - el[1])
#            print(f"mapped to: {newval}")
            break
        else:
            continue

    for el in map_dict['temperature_map']:
#        print(f"testing {newval} temperature map")

#        print(f"element: {el}")
        lower_limit = el[0]
        upper_limit = lower_limit + el[2] - 1
        if newval >= lower_limit and newval <= upper_limit: 
#            print(f"temperature_map testval: {newval} in range of {lower_limit} - {upper_limit}")
            if lower_limit < el[1]:
                newval = newval + (el[1] - lower_limit)
            else:
                newval = newval - (lower_limit - el[1])
 #           print(f"mapped to: {newval}")
            break
        else:
            continue
        
    for el in map_dict['light_map']:
#        print(f"testing {newval} light map")

#        print(f"element: {el}")
        lower_limit = el[0]
        upper_limit = lower_limit + el[2] - 1
        if newval >= lower_limit and newval <= upper_limit: 
 #           print(f"light_map testval: {newval} in range of {lower_limit} - {upper_limit}")
            if lower_limit < el[1]:
                newval = newval + (el[1] - lower_limit)
            else:
                newval = newval - (lower_limit - el[1])
 #           print(f"mapped to: {newval}")
            break
        else:
            continue
        
    for el in map_dict['water_map']:
#        print(f"testing {newval} light map")

#        print(f"element: {el}")
        lower_limit = el[0]
        upper_limit = lower_limit + el[2] - 1
        if newval >= lower_limit and newval <= upper_limit: 
 #           print(f"water_map testval: {newval} in range of {lower_limit} - {upper_limit}")
            if lower_limit < el[1]:
                newval = newval + (el[1] - lower_limit)
            else:
                newval = newval - (lower_limit - el[1])
 #           print(f"mapped to: {newval}")
            break
        else:
            continue
        
    for el in map_dict['fertilizer_map']:
#        print(f"testing {newval} fertilizer map")
#        print(f"element: {el}")
        lower_limit = el[0]
        upper_limit = lower_limit + el[2] - 1
        if newval >= lower_limit and newval <= upper_limit: 
 #           print(f"fertilizer_map testval: {newval} in range of {lower_limit} - {upper_limit}")
            if lower_limit < el[1]:
                newval = newval + (el[1] - lower_limit)
            else:
                newval = newval - (lower_limit - el[1])
 #           print(f"mapped to: {newval}")
            break
        else:
            continue
        
    for el in map_dict['soil_map']:
#        print(f"testing {newval} soil map")
#        print(f"element: {el}")
        lower_limit = el[0]
        upper_limit = lower_limit + el[2] - 1
        if newval >= lower_limit and newval <= upper_limit: 
 #           print(f"soil_map testval: {newval} in range of {lower_limit} - {upper_limit}")
            if lower_limit < el[1]:
                newval = newval + (el[1] - lower_limit)
            else:
                newval = newval - (lower_limit - el[1])
 #           print(f"mapped to: {newval}")
            break
        else:
            continue
        
#    print(f"Seeds: {seeds}")
    for i,k in zip(seeds[0::2], seeds[1::2]):
        if newval >= i and newval <= i+k-1:
            print(f"Hit on {newval} at {x}")
            a_seed = True
            break
        else:
            continue
#            print(f"No hit on {newval}")

