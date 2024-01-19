# Don't panic! 
# It's just a program
# AOC 2023 Day 5 Part 1

import re

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

map_categories = ['soil_map','fertilizer_map','water_map','light_map','temperature_map','humidity_map','location_map']
map_dict = {}  # Create a dictionary to store the lists

seeds_regexp = re.compile(r"seeds:")

with open('/home/opalko/Desktop/Python Projects/Advent of Code 2023/day5/day5-data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    lines = [i for a, i in enumerate(lines) if i != '']
    print(lines)

for line in lines:
    seeds_r = re.split(seeds_regexp, line)
    if len(seeds_r) > 1:  # Check if the split produced at least two elements
        seeds.extend(seeds_r[1].split())
    
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
print(location_map)
print("Don't panic!")

# Process raw strings from the data file to create number_lists
for map_type in map_categories:
    number_lists = []  
    for map in eval(map_type):
        numbers = [int(number) for number in map.split()]  # Split and convert
        number_lists.append(numbers)  # Append the list of integers
    map_dict[map_type] = number_lists  # Assign to the dictionary
    print(f"{map_type} is {map_dict[map_type]}")
    print(map_dict)

#for map_type in map_categories:
#    numbers = map_dict[map_type]
#    print(numbers)
###################################################################
for map in map_dict['soil_map']:
#     print(map)
    for i in range(len(seeds)):
        seed = seeds[i]
 #       print(f"Comparing: {seed} if in range of {map[1]} - {int(map[1])+int(map[2])}")
        if int(seed) in range(int(map[1]), int(map[1]) + int(map[2])):  
#            print(f"{seed} in {map[1]} - {int(map[1])+int(map[2])}")
            equivalent = int(seed) - int(map[1]) + int(map[0])
            soil_list.append(equivalent)
            temp_list.append(seed)
for element in seeds:
    if element not in temp_list:
        soil_list.append(int(element))
soil_list.sort()
print(f"soil list {soil_list}")        
seed = 0
temp_list = []
for map in map_dict['fertilizer_map']:
#     print(map)
    for seed in soil_list:
 #       print(f"Comparing: {seed} if in range of {map[1]} - {int(map[1])+int(map[2])}")
        if int(seed) in range(int(map[1]), int(map[1]) + int(map[2])):  
#            print(f"{seed} in {map[1]} - {int(map[1])+int(map[2])}")
            equivalent = int(seed) - int(map[1]) + int(map[0])
            fertilizer_list.append(equivalent)
            temp_list.append(seed)
            # print(soil_list)
for element in soil_list:
    if element not in temp_list:
        fertilizer_list.append(element)
fertilizer_list.sort()
print(f"fertilizer_list: {fertilizer_list}") 
seed = 0
temp_list = []
for map in map_dict['water_map']:
#     print(map)
    for seed in fertilizer_list:
 #       print(f"Comparing: {seed} if in range of {map[1]} - {int(map[1])+int(map[2])}")
        if int(seed) in range(int(map[1]), int(map[1]) + int(map[2])):  
#            print(f"{seed} in {map[1]} - {int(map[1])+int(map[2])}")
            equivalent = int(seed) - int(map[1]) + int(map[0])
            water_list.append(equivalent)
            temp_list.append(seed)
            # print(soil_list)
for element in fertilizer_list:
    if element not in temp_list:
        water_list.append(element)
water_list.sort()
print(f"water_list: {water_list}") 
seed = 0
temp_list = []
for map in map_dict['light_map']:
#     print(map)
    for seed in water_list:
#        print(f"Comparing: {seed} if in range of {map[1]} - {int(map[1])+int(map[2])}")
        if int(seed) in range(int(map[1]), int(map[1]) + int(map[2])):  
#            print(f"{seed} in {map[1]} - {int(map[1])+int(map[2])}")
            equivalent = int(seed) - int(map[1]) + int(map[0])
            light_list.append(equivalent)
            temp_list.append(seed)
            # print(soil_list)
for element in water_list:
    if element not in temp_list:
        light_list.append(element)
light_list.sort()
print(f"light_list: {light_list}")        
seed = 0
temp_list = []
for map in map_dict['temperature_map']:
 #   print(map)
    for seed in light_list:
 #       print(f"Comparing: {seed} if in range of {map[1]} - {int(map[1])+int(map[2])}")
        if int(seed) in range(int(map[1]), int(map[1]) + int(map[2])):  
#            print(f"{seed} in {map[1]} - {int(map[1])+int(map[2])}")
            equivalent = int(seed) - int(map[1]) + int(map[0])
            temperature_list.append(equivalent)
            temp_list.append(seed)
            # print(soil_list)
for element in light_list:
    if element not in temp_list:
        temperature_list.append(element)
temperature_list.sort()
print(f"temperature_list: {temperature_list}")        
seed = 0
temp_list = []
for map in map_dict['humidity_map']:
 #   print(map)
    for seed in temperature_list:
 #       print(f"Comparing: {seed} if in range of {map[1]} - {int(map[1])+int(map[2])}")
        if int(seed) in range(int(map[1]), int(map[1]) + int(map[2])):  
#            print(f"{seed} in {map[1]} - {int(map[1])+int(map[2])}")
            equivalent = int(seed) - int(map[1]) + int(map[0])
            humidity_list.append(equivalent)
            temp_list.append(seed)
            # print(soil_list)
for element in temperature_list:
    if element not in temp_list:
        humidity_list.append(element)
humidity_list.sort()
print(f"humidity_list: {humidity_list}")    
seed = 0
temp_list = []
for map in map_dict['location_map']:
#     print(map)
    for seed in humidity_list:
 #       print(f"Comparing: {seed} if in range of {map[1]} - {int(map[1])+int(map[2])}")
        if int(seed) in range(int(map[1]), int(map[1]) + int(map[2])):  
#            print(f"{seed} in {map[1]} - {int(map[1])+int(map[2])}")
            equivalent = int(seed) - int(map[1]) + int(map[0])
            location_list.append(equivalent)
            temp_list.append(seed)
            # print(soil_list)
for element in humidity_list:
    if element not in temp_list:
        location_list.append(element)
location_list.sort()
print(f"location list: {location_list}")   
min = min(location_list)
print(f"Minimum: {min}")     

