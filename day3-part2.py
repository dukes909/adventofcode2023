import re

num=0
sum = 0

number_regex = re.compile(r"(\d+)")
star_regex = re.compile(r"(\*)")

def find_matches(star_tuple, line_up, line_center, line_down):
     
     range_set = [-1,0,1]
     star_tuple_plus_1 = star_tuple
     pos_left = star_tuple[0] - 1
     pos_right = star_tuple[1]
     number_range = range(part_location[0], part_location[1])

     for a_number in line_up:
        part_range = range(part_location[0], part_location[1])
 


with open('day3-data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
#    print(lines)
    distances = [-1,0,1]
    total = 0
    top = 0
    bottom = len(lines)
    left = 0
    right = len(lines[0])
    
    ### Calculate sum products in horizontally adjacent numbers
    for i, line in enumerate(lines):
        print(i,line)
        
        numbers_matched = 0
        all_matches = []
 
        numbers_this_row = list(re.finditer(number_regex, line))
        if i > top:
            numbers_row_above = list(re.finditer(number_regex, lines[i-1]))
        else:
            numbers_row_above = []
        if i < bottom - 1:
            numbers_row_below = list(re.finditer(number_regex, lines[i+1]))
        else:
            numbers_row_below = []

        stars_this_row = list(re.finditer(star_regex, line))
    
        for star in stars_this_row:
            numbers_matched = 0
            all_matches = []
            print(f"star span: {star.span()}")
            star_pos = star.span()
            print(star_pos)
            for number in numbers_this_row:
                numbers_pos = number.span()
                print(numbers_pos)
                numbers_range = range(numbers_pos[0], numbers_pos[1])
                print(numbers_range)
                if any(star_pos[0] - num in distances for num in numbers_range):

                if star_pos in numbers_range:
                    print(f"Match at ")

            product = find_matches(star_pos,  
                         numbers_row_above, 
                         numbers_this_row, 
                         numbers_row_below
                         )

#                 if any(star.span()[0] - num in distances for num in numbers_range):
#                     numbers_matched += 1
#                     all_matches.append(number.group())
#                     print(f"same line : {all_matches}")
#                     if numbers_matched == 2:
#                             row_product = int(all_matches[0]) * int(all_matches[1])
#                             total += row_product
#                             numbers_matched = 0
#                             all_matches = []

# ### ROW ABOVE
#             if i > top:
#                     numbers_in_row_above = list(re.finditer(number_regex, lines[i-1]))
#                     for number in numbers_in_row_above:
#                         numbers_pos = number.span()
#                         numbers_range = range(numbers_pos[0], numbers_pos[1])
#                         if any(star.span()[0] - num in distances for num in numbers_range):
#                             numbers_matched += 1
#                             all_matches.append(number.group())
#                             print(f"above : {all_matches}")
#                             if numbers_matched == 2:
#                                 row_product = int(all_matches[0]) * int(all_matches[1])
#                                 total += row_product
#                                 numbers_matched = 0
#                                 all_matches = []

#  ### ROW BELOW                             
#             if i < bottom -1:
#                     numbers_in_row_below = list(re.finditer(number_regex, lines[i+1]))
#                     for number in numbers_in_row_below:
#                         numbers_pos = number.span()
#                         numbers_range = range(numbers_pos[0], numbers_pos[1])
#                         if any(star.span()[0] - num in distances for num in numbers_range):
#                             numbers_matched += 1
#                             all_matches.append(number.group())
#                             print(f"below :{all_matches}")                    
#                             if numbers_matched == 2:
#                                 row_product = int(all_matches[0]) * int(all_matches[1])
#                                 total += row_product
#                                 numbers_matched = 0
#                                 all_matches = []



                            
#         if numbers_matched == 2:
#             row_product = int(all_matches[0]) * int(all_matches[1])
#             total += row_product
# print(total)



 #       print([match.group() for match in stars])
 #       all_numbers = [match.group() for matches in [numbers] for match in matches]
        # for j,tuple in enumerate(number_indices):
            
 